# Graph Structure Analysis Report

## Overview

This report analyzes how the scene graph structure changes across different granularity levels.

---

## Statistics by Granularity Level

### FINE-Grained

- **Nodes**: 19
- **Edges**: 21
- **Total Objects Represented**: 24
- **Average Degree**: 2.21
- **Graph Density**: 0.061

**Most Connected Nodes**:
- person (degree: 14, objects: 3)
- skate park (degree: 3, objects: 1)
- shirt (degree: 3, objects: 2)
- bench (degree: 2, objects: 1)
- skateboard (degree: 2, objects: 2)

### MID-Grained

- **Nodes**: 10
- **Edges**: 13
- **Total Objects Represented**: 24
- **Average Degree**: 2.60
- **Graph Density**: 0.144

**Most Connected Nodes**:
- organism (degree: 9, objects: 6)
- artifact (degree: 5, objects: 4)
- instrumentality (degree: 2, objects: 5)
- dark (degree: 2, objects: 1)
- skate park (degree: 2, objects: 1)

### COARSE-Grained

- **Nodes**: 5
- **Edges**: 4
- **Total Objects Represented**: 24
- **Average Degree**: 1.60
- **Graph Density**: 0.200

**Most Connected Nodes**:
- object (degree: 4, objects: 19)
- state (degree: 1, objects: 1)
- skate park (degree: 1, objects: 1)
- thing (degree: 1, objects: 1)
- abstraction (degree: 1, objects: 2)

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
