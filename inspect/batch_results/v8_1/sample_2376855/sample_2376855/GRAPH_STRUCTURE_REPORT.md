# Graph Structure Analysis Report

## Overview

This report analyzes how the scene graph structure changes across different granularity levels.

---

## Statistics by Granularity Level

### FINE-Grained

- **Nodes**: 23
- **Edges**: 10
- **Total Objects Represented**: 32
- **Average Degree**: 0.87
- **Graph Density**: 0.020

**Most Connected Nodes**:
- cell phone (degree: 2, objects: 2)
- man (degree: 2, objects: 1)
- hand (degree: 2, objects: 1)
- phone (degree: 2, objects: 3)
- thumb (degree: 2, objects: 2)

### MID-Grained

- **Nodes**: 18
- **Edges**: 9
- **Total Objects Represented**: 32
- **Average Degree**: 1.00
- **Graph Density**: 0.029

**Most Connected Nodes**:
- extremity (degree: 3, objects: 5)
- cell phone (degree: 2, objects: 2)
- equipment (degree: 2, objects: 4)
- person (degree: 2, objects: 1)
- artifact (degree: 2, objects: 3)

### COARSE-Grained

- **Nodes**: 8
- **Edges**: 6
- **Total Objects Represented**: 32
- **Average Degree**: 1.50
- **Graph Density**: 0.107

**Most Connected Nodes**:
- physical entity (degree: 4, objects: 11)
- object (degree: 3, objects: 13)
- communicate (degree: 2, objects: 2)
- abstraction (degree: 1, objects: 2)
- pointer finger (degree: 1, objects: 1)

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
