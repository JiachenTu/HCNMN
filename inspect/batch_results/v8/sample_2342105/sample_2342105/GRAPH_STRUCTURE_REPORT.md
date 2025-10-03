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

- **Nodes**: 20
- **Edges**: 21
- **Total Objects Represented**: 28
- **Average Degree**: 2.10
- **Graph Density**: 0.055

**Most Connected Nodes**:
- document (degree: 6, objects: 6)
- person (degree: 6, objects: 3)
- land (degree: 5, objects: 1)
- atmosphere (degree: 4, objects: 1)
- organism (degree: 3, objects: 1)

### COARSE-Grained

- **Nodes**: 13
- **Edges**: 16
- **Total Objects Represented**: 28
- **Average Degree**: 2.46
- **Graph Density**: 0.103

**Most Connected Nodes**:
- object (degree: 8, objects: 6)
- matter (degree: 5, objects: 1)
- abstraction (degree: 5, objects: 4)
- physical entity (degree: 4, objects: 4)
- communication (degree: 2, objects: 5)

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
