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

- **Nodes**: 16
- **Edges**: 9
- **Total Objects Represented**: 35
- **Average Degree**: 1.12
- **Graph Density**: 0.037

**Most Connected Nodes**:
- container (degree: 4, objects: 5)
- furnishing (degree: 2, objects: 4)
- plant (degree: 2, objects: 6)
- table (degree: 2, objects: 2)
- organism (degree: 1, objects: 5)

### COARSE-Grained

- **Nodes**: 6
- **Edges**: 3
- **Total Objects Represented**: 35
- **Average Degree**: 1.00
- **Graph Density**: 0.100

**Most Connected Nodes**:
- physical entity (degree: 3, objects: 15)
- object (degree: 2, objects: 13)
- abstraction (degree: 1, objects: 4)
- attribute (degree: 0, objects: 1)
- babys breath (degree: 0, objects: 1)

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
