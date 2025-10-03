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

- **Nodes**: 14
- **Edges**: 9
- **Total Objects Represented**: 35
- **Average Degree**: 1.29
- **Graph Density**: 0.049

**Most Connected Nodes**:
- instrumentality (degree: 6, objects: 9)
- organism (degree: 3, objects: 11)
- table (degree: 2, objects: 2)
- structure (degree: 1, objects: 2)
- covering (degree: 1, objects: 2)

### COARSE-Grained

- **Nodes**: 5
- **Edges**: 2
- **Total Objects Represented**: 35
- **Average Degree**: 0.80
- **Graph Density**: 0.100

**Most Connected Nodes**:
- object (degree: 2, objects: 27)
- abstraction (degree: 1, objects: 5)
- thing (degree: 1, objects: 1)
- babys breath (degree: 0, objects: 1)
- chair back (degree: 0, objects: 1)

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
