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

- **Nodes**: 17
- **Edges**: 20
- **Total Objects Represented**: 36
- **Average Degree**: 2.35
- **Graph Density**: 0.074

**Most Connected Nodes**:
- plant organ (degree: 7, objects: 9)
- plant (degree: 7, objects: 2)
- plant part (degree: 5, objects: 1)
- language unit (degree: 5, objects: 4)
- physical condition (degree: 3, objects: 5)

### COARSE-Grained

- **Nodes**: 10
- **Edges**: 18
- **Total Objects Represented**: 36
- **Average Degree**: 3.60
- **Graph Density**: 0.200

**Most Connected Nodes**:
- object (degree: 9, objects: 12)
- banana (degree: 7, objects: 2)
- location (degree: 4, objects: 4)
- part (degree: 4, objects: 4)
- fruit (degree: 4, objects: 2)

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
