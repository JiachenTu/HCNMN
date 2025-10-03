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

- **Nodes**: 13
- **Edges**: 8
- **Total Objects Represented**: 32
- **Average Degree**: 1.23
- **Graph Density**: 0.051

**Most Connected Nodes**:
- organism (degree: 3, objects: 2)
- external body part (degree: 3, objects: 5)
- cell phone (degree: 2, objects: 2)
- instrumentality (degree: 2, objects: 11)
- artifact (degree: 1, objects: 3)

### COARSE-Grained

- **Nodes**: 8
- **Edges**: 5
- **Total Objects Represented**: 32
- **Average Degree**: 1.25
- **Graph Density**: 0.089

**Most Connected Nodes**:
- object (degree: 3, objects: 16)
- thing (degree: 3, objects: 8)
- communicate (degree: 1, objects: 2)
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
