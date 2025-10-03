# Graph Structure Analysis Report

## Overview

This report analyzes how the scene graph structure changes across different granularity levels.

---

## Statistics by Granularity Level

### FINE-Grained

- **Nodes**: 22
- **Edges**: 23
- **Total Objects Represented**: 28
- **Average Degree**: 2.09
- **Graph Density**: 0.050

**Most Connected Nodes**:
- sky (degree: 5, objects: 1)
- kites (degree: 5, objects: 1)
- ground (degree: 5, objects: 1)
- woman (degree: 5, objects: 2)
- boy (degree: 3, objects: 1)

### MID-Grained

- **Nodes**: 19
- **Edges**: 21
- **Total Objects Represented**: 28
- **Average Degree**: 2.21
- **Graph Density**: 0.061

**Most Connected Nodes**:
- person (degree: 9, objects: 4)
- document (degree: 6, objects: 6)
- land (degree: 5, objects: 1)
- sky (degree: 4, objects: 1)
- cone (degree: 2, objects: 1)

### COARSE-Grained

- **Nodes**: 10
- **Edges**: 12
- **Total Objects Represented**: 28
- **Average Degree**: 2.40
- **Graph Density**: 0.133

**Most Connected Nodes**:
- physical entity (degree: 6, objects: 7)
- object (degree: 6, objects: 6)
- abstraction (degree: 5, objects: 8)
- group (degree: 1, objects: 1)
- ladybug kites (degree: 1, objects: 1)

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
