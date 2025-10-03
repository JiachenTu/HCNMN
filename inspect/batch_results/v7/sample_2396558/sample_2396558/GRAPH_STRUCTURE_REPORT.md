# Graph Structure Analysis Report

## Overview

This report analyzes how the scene graph structure changes across different granularity levels.

---

## Statistics by Granularity Level

### FINE-Grained

- **Nodes**: 21
- **Edges**: 23
- **Total Objects Represented**: 36
- **Average Degree**: 2.19
- **Graph Density**: 0.055

**Most Connected Nodes**:
- banana (degree: 7, objects: 2)
- apple (degree: 5, objects: 1)
- stem (degree: 5, objects: 4)
- lemon (degree: 4, objects: 3)
- fruit (degree: 4, objects: 2)

### MID-Grained

- **Nodes**: 15
- **Edges**: 18
- **Total Objects Represented**: 36
- **Average Degree**: 2.40
- **Graph Density**: 0.086

**Most Connected Nodes**:
- natural object (degree: 8, objects: 10)
- organism (degree: 7, objects: 2)
- word (degree: 5, objects: 4)
- physical condition (degree: 3, objects: 5)
- topographic point (degree: 3, objects: 3)

### COARSE-Grained

- **Nodes**: 5
- **Edges**: 7
- **Total Objects Represented**: 36
- **Average Degree**: 2.80
- **Graph Density**: 0.350

**Most Connected Nodes**:
- object (degree: 6, objects: 20)
- abstraction (degree: 3, objects: 9)
- state (degree: 3, objects: 5)
- thing (degree: 1, objects: 1)
- process (degree: 1, objects: 1)

---

## Graph Merging Analysis

### Edge Reduction

As granularity becomes coarser:
- Objects merge into concepts
- Edges between objects of the same concept become self-loops (removed)
- Multiple edges between merged concepts are collapsed (weight increases)

### Information Loss

The reduction in edges represents relationships that become internalized when objects merge.
This is expected and demonstrates the abstraction at work.

---

**Note**: Graph visualizations show only inter-concept relationships.
Intra-concept relationships (within merged groups) are not shown but are preserved in the hierarchy.
