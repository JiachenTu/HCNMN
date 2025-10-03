# Graph Structure Analysis Report

## Overview

This report analyzes how the scene graph structure changes across different granularity levels.

---

## Statistics by Granularity Level

### FINE-Grained

- **Nodes**: 9
- **Edges**: 3
- **Total Objects Represented**: 26
- **Average Degree**: 0.67
- **Graph Density**: 0.042

**Most Connected Nodes**:
- car (degree: 2, objects: 8)
- street. (degree: 1, objects: 1)
- street (degree: 1, objects: 3)
- window (degree: 1, objects: 8)
- building (degree: 1, objects: 2)

### MID-Grained

- **Nodes**: 8
- **Edges**: 2
- **Total Objects Represented**: 26
- **Average Degree**: 0.50
- **Graph Density**: 0.036

**Most Connected Nodes**:
- artifact (degree: 2, objects: 8)
- street. (degree: 1, objects: 1)
- road (degree: 1, objects: 3)
- stairway (degree: 0, objects: 1)
- way (degree: 0, objects: 1)

### COARSE-Grained

- **Nodes**: 3
- **Edges**: 2
- **Total Objects Represented**: 26
- **Average Degree**: 1.33
- **Graph Density**: 0.333

**Most Connected Nodes**:
- physical entity (degree: 2, objects: 16)
- object (degree: 1, objects: 9)
- street. (degree: 1, objects: 1)

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
