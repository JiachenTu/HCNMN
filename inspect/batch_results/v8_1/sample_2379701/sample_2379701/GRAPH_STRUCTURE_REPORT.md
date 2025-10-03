# Graph Structure Analysis Report

## Overview

This report analyzes how the scene graph structure changes across different granularity levels.

---

## Statistics by Granularity Level

### FINE-Grained

- **Nodes**: 18
- **Edges**: 15
- **Total Objects Represented**: 19
- **Average Degree**: 1.67
- **Graph Density**: 0.049

**Most Connected Nodes**:
- woman (degree: 6, objects: 1)
- ball (degree: 2, objects: 1)
- air (degree: 2, objects: 1)
- shirt (degree: 2, objects: 1)
- ground (degree: 2, objects: 1)

### MID-Grained

- **Nodes**: 17
- **Edges**: 15
- **Total Objects Represented**: 19
- **Average Degree**: 1.76
- **Graph Density**: 0.055

**Most Connected Nodes**:
- person (degree: 6, objects: 1)
- artifact (degree: 4, objects: 2)
- air (degree: 2, objects: 1)
- land (degree: 2, objects: 1)
- background (degree: 2, objects: 1)

### COARSE-Grained

- **Nodes**: 3
- **Edges**: 4
- **Total Objects Represented**: 19
- **Average Degree**: 2.67
- **Graph Density**: 0.667

**Most Connected Nodes**:
- object (degree: 3, objects: 6)
- abstraction (degree: 3, objects: 7)
- physical entity (degree: 2, objects: 6)

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
