# Graph Structure Analysis Report

## Overview

This report analyzes how the scene graph structure changes across different granularity levels.

---

## Statistics by Granularity Level

### FINE-Grained

- **Nodes**: 13
- **Edges**: 10
- **Total Objects Represented**: 14
- **Average Degree**: 1.54
- **Graph Density**: 0.064

**Most Connected Nodes**:
- cabinet (degree: 4, objects: 1)
- toilet (degree: 3, objects: 1)
- sink (degree: 3, objects: 1)
- wall (degree: 2, objects: 1)
- door (degree: 2, objects: 1)

### MID-Grained

- **Nodes**: 6
- **Edges**: 7
- **Total Objects Represented**: 14
- **Average Degree**: 2.33
- **Graph Density**: 0.233

**Most Connected Nodes**:
- structure (degree: 5, objects: 4)
- artifact (degree: 3, objects: 4)
- instrumentality (degree: 3, objects: 2)
- handle (degree: 1, objects: 2)
- action (degree: 1, objects: 1)

### COARSE-Grained

- **Nodes**: 3
- **Edges**: 2
- **Total Objects Represented**: 14
- **Average Degree**: 1.33
- **Graph Density**: 0.333

**Most Connected Nodes**:
- object (degree: 2, objects: 12)
- abstraction (degree: 1, objects: 1)
- thing (degree: 1, objects: 1)

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
