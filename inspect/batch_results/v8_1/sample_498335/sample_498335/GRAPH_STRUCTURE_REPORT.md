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

- **Nodes**: 15
- **Edges**: 10
- **Total Objects Represented**: 30
- **Average Degree**: 1.33
- **Graph Density**: 0.048

**Most Connected Nodes**:
- boundary (degree: 3, objects: 2)
- artifact (degree: 2, objects: 8)
- structure (degree: 2, objects: 2)
- road (degree: 2, objects: 1)
- instrumentality (degree: 2, objects: 2)

### COARSE-Grained

- **Nodes**: 4
- **Edges**: 3
- **Total Objects Represented**: 30
- **Average Degree**: 1.50
- **Graph Density**: 0.250

**Most Connected Nodes**:
- object (degree: 2, objects: 10)
- physical entity (degree: 2, objects: 12)
- abstraction (degree: 1, objects: 3)
- communication (degree: 1, objects: 5)

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
