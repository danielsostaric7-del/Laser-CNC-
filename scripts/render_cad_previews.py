"""Render quick-look PNGs from supplied STEP files.

The authoritative design files remain the SOLIDWORKS files under ``cad/``.
The repository intentionally keeps only selected neutral models, so each input
is optional and only the requested preview group is rendered.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from OCP.BRep import BRep_Tool
from OCP.BRepMesh import BRepMesh_IncrementalMesh
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.TDF import TDF_LabelSequence
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.TopAbs import TopAbs_ShapeEnum
from OCP.TopExp import TopExp_Explorer
from OCP.TopoDS import TopoDS
from OCP.TopLoc import TopLoc_Location
from OCP.XCAFDoc import XCAFDoc_DocumentTool


BACKGROUND = "#0b1220"
OBJECT = (0.56, 0.66, 0.77)
EDGE = (0.12, 0.18, 0.26, 0.55)


def load_step_shape(path: Path):
    """Load the first free shape from a STEP file using the assembly-aware reader."""

    document = TDocStd_Document(TCollection_ExtendedString("cad-preview"))
    reader = STEPCAFControl_Reader()
    reader.SetColorMode(True)
    status = reader.ReadFile(str(path))
    if not status:
        raise RuntimeError(f"Could not read STEP file: {path}")
    if not reader.Transfer(document):
        raise RuntimeError(f"Could not transfer STEP geometry: {path}")

    shape_tool = XCAFDoc_DocumentTool.ShapeTool_s(document.Main())
    labels = TDF_LabelSequence()
    shape_tool.GetFreeShapes(labels)
    if labels.Length() == 0:
        raise RuntimeError(f"STEP file contained no displayable shapes: {path}")
    return shape_tool.GetShape_s(labels.Value(1))


def mesh_shape(shape, deflection: float = 0.65):
    """Return triangle vertices and a simple per-triangle lighting value."""

    BRepMesh_IncrementalMesh(shape, deflection)
    explorer = TopExp_Explorer(shape, TopAbs_ShapeEnum.TopAbs_FACE)
    triangles = []
    while explorer.More():
        face = TopoDS.Face_s(explorer.Current())
        location = TopLoc_Location()
        triangulation = BRep_Tool.Triangulation_s(face, location)
        if triangulation:
            transform = location.Transformation()
            nodes = {}
            for index in range(1, triangulation.NbNodes() + 1):
                point = triangulation.Node(index).Transformed(transform)
                nodes[index] = (point.X(), point.Y(), point.Z())

            for index in range(1, triangulation.NbTriangles() + 1):
                a, b, c = triangulation.Triangle(index).Get()
                triangle = [nodes[a], nodes[b], nodes[c]]
                ux = triangle[1][0] - triangle[0][0]
                uy = triangle[1][1] - triangle[0][1]
                uz = triangle[1][2] - triangle[0][2]
                vx = triangle[2][0] - triangle[0][0]
                vy = triangle[2][1] - triangle[0][1]
                vz = triangle[2][2] - triangle[0][2]
                nx = uy * vz - uz * vy
                ny = uz * vx - ux * vz
                nz = ux * vy - uy * vx
                length = math.sqrt(nx * nx + ny * ny + nz * nz) or 1.0
                light = abs((nx * 0.45 + ny * -0.55 + nz * 0.72) / length)
                triangles.append((triangle, max(0.22, min(1.0, 0.32 + 0.68 * light))))
        explorer.Next()
    if not triangles:
        raise RuntimeError("The STEP shape produced no triangles")
    return triangles


def shaded_color(level: float):
    return tuple(min(1.0, channel * (0.72 + 0.32 * level)) for channel in OBJECT)


def render(triangles, output: Path, title: str, subtitle: str, elev: float, azim: float):
    points = [point for triangle, _ in triangles for point in triangle]
    xs, ys, zs = zip(*points)
    mins = (min(xs), min(ys), min(zs))
    maxs = (max(xs), max(ys), max(zs))
    spans = [maxs[i] - mins[i] for i in range(3)]
    center = [(mins[i] + maxs[i]) / 2 for i in range(3)]
    radius = max(spans) * 0.58

    figure = plt.figure(figsize=(12, 7.5), dpi=160, facecolor=BACKGROUND)
    axis = figure.add_subplot(111, projection="3d")
    axis.set_facecolor(BACKGROUND)
    axis.view_init(elev=elev, azim=azim)
    axis.set_xlim(center[0] - radius, center[0] + radius)
    axis.set_ylim(center[1] - radius, center[1] + radius)
    axis.set_zlim(center[2] - radius, center[2] + radius)
    axis.set_box_aspect((max(spans[0], 1), max(spans[1], 1), max(spans[2], 1)))
    axis.set_axis_off()

    polygons = [triangle for triangle, _ in triangles]
    colors = [shaded_color(level) for _, level in triangles]
    collection = Poly3DCollection(
        polygons,
        facecolors=colors,
        edgecolors=EDGE,
        linewidths=0.12,
        antialiased=True,
    )
    axis.add_collection3d(collection)
    figure.text(0.055, 0.925, title, color="#f4f7fb", fontsize=22, weight="bold")
    figure.text(0.055, 0.885, subtitle, color="#9db0c6", fontsize=11)
    figure.subplots_adjust(left=0, right=1, bottom=0, top=1)
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=160, facecolor=BACKGROUND)
    plt.close(figure)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cage", type=Path)
    parser.add_argument("--laser", type=Path)
    parser.add_argument("--adapter", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if not any((args.cage, args.laser, args.adapter)):
        parser.error("provide at least one of --cage, --laser, or --adapter")

    args.output.mkdir(parents=True, exist_ok=True)
    views = {}
    if args.cage:
        cage = mesh_shape(load_step_shape(args.cage))
        views.update({
            "cad-cage-isometric.png": (30, -55, "CNC cage assembly", "STEP preview exported from the SOLIDWORKS design", cage),
            "cad-cage-front.png": (8, -90, "CNC cage assembly · front", "Front orthographic-style view", cage),
            "cad-cage-right.png": (8, 0, "CNC cage assembly · right", "Right orthographic-style view", cage),
            "cad-cage-top.png": (86, -90, "CNC cage assembly · top", "Top orthographic-style view", cage),
            "cad-cage-rear.png": (8, 90, "CNC cage assembly · rear", "Rear orthographic-style view", cage),
            "cad-cage-left.png": (8, 180, "CNC cage assembly · left", "Left orthographic-style view", cage),
        })
    if args.laser:
        laser = mesh_shape(load_step_shape(args.laser))
        views["cad-laser-module.png"] = (24, -55, "LaserTree module", "STEP preview from the project CAD exports", laser)
    if args.adapter:
        adapter = mesh_shape(load_step_shape(args.adapter))
        views["cad-driver-adapter.png"] = (28, -55, "Laser driver adapter", "P-DA-01 STEP preview from the project CAD exports", adapter)
    for filename, (elev, azim, title, subtitle, triangles) in views.items():
        render(triangles, args.output / filename, title, subtitle, elev, azim)


if __name__ == "__main__":
    main()
