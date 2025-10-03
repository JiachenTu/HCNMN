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

- **Nodes**: 16
- **Edges**: 14
- **Total Objects Represented**: 19
- **Average Degree**: 1.75
- **Graph Density**: 0.058

**Most Connected Nodes**:
- living thing (degree: 5, objects: 1)
- commodity (degree: 2, objects: 2)
- artifact (degree: 2, objects: 1)
- air (degree: 2, objects: 1)
- body part (degree: 2, objects: 2)

### COARSE-Grained

- **Nodes**: 6
- **Edges**: 10
- **Total Objects Represented**: 19
- **Average Degree**: 3.33
- **Graph Density**: 0.333

**Most Connected Nodes**:
- object (degree: 7, objects: 7)
- physical entity (degree: 4, objects: 4)
- abstraction (degree: 4, objects: 5)
- matter (degree: 2, objects: 1)
- attribute (degree: 2, objects: 1)

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
