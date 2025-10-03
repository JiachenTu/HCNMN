# Graph Structure Analysis Report

## Overview

This report analyzes how the scene graph structure changes across different granularity levels.

---

## Statistics by Granularity Level

### FINE-Grained

- **Nodes**: 19
- **Edges**: 9
- **Total Objects Represented**: 35
- **Average Degree**: 0.95
- **Graph Density**: 0.026

**Most Connected Nodes**:
- vase (degree: 4, objects: 5)
- flowers (degree: 2, objects: 6)
- table (degree: 2, objects: 2)
- flower (degree: 1, objects: 5)
- drawer (degree: 1, objects: 2)

### MID-Grained

- **Nodes**: 15
- **Edges**: 9
- **Total Objects Represented**: 35
- **Average Degree**: 1.20
- **Graph Density**: 0.043

**Most Connected Nodes**:
- container (degree: 4, objects: 5)
- plant (degree: 3, objects: 11)
- furnishing (degree: 2, objects: 4)
- table (degree: 2, objects: 2)
- artifact (degree: 1, objects: 2)

### COARSE-Grained

- **Nodes**: 8
- **Edges**: 5
- **Total Objects Represented**: 35
- **Average Degree**: 1.25
- **Graph Density**: 0.089

**Most Connected Nodes**:
- object (degree: 4, objects: 19)
- physical entity (degree: 2, objects: 4)
- group (degree: 2, objects: 3)
- flower (degree: 1, objects: 5)
- abstraction (degree: 1, objects: 1)

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
