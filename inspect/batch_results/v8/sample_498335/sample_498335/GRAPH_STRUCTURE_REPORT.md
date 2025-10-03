# Graph Structure Analysis Report

## Overview

This report analyzes how the scene graph structure changes across different granularity levels.

---

## Statistics by Granularity Level

### FINE-Grained

- **Nodes**: 18
- **Edges**: 10
- **Total Objects Represented**: 30
- **Average Degree**: 1.11
- **Graph Density**: 0.033

**Most Connected Nodes**:
- edge (degree: 3, objects: 2)
- street (degree: 2, objects: 1)
- flowers (degree: 1, objects: 2)
- pot (degree: 1, objects: 2)
- billboard (degree: 1, objects: 1)

### MID-Grained

- **Nodes**: 13
- **Edges**: 10
- **Total Objects Represented**: 30
- **Average Degree**: 1.54
- **Graph Density**: 0.064

**Most Connected Nodes**:
- artifact (degree: 3, objects: 9)
- structure (degree: 3, objects: 3)
- region (degree: 3, objects: 2)
- road (degree: 2, objects: 1)
- plant (degree: 1, objects: 3)

### COARSE-Grained

- **Nodes**: 8
- **Edges**: 7
- **Total Objects Represented**: 30
- **Average Degree**: 1.75
- **Graph Density**: 0.125

**Most Connected Nodes**:
- object (degree: 4, objects: 11)
- physical entity (degree: 2, objects: 7)
- communication (degree: 2, objects: 6)
- location (degree: 2, objects: 2)
- indefinite quantity (degree: 1, objects: 1)

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
