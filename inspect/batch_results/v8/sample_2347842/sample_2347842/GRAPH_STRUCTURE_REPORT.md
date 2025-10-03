# Graph Structure Analysis Report

## Overview

This report analyzes how the scene graph structure changes across different granularity levels.

---

## Statistics by Granularity Level

### FINE-Grained

- **Nodes**: 19
- **Edges**: 21
- **Total Objects Represented**: 24
- **Average Degree**: 2.21
- **Graph Density**: 0.061

**Most Connected Nodes**:
- person (degree: 14, objects: 3)
- skate park (degree: 3, objects: 1)
- shirt (degree: 3, objects: 2)
- bench (degree: 2, objects: 1)
- skateboard (degree: 2, objects: 2)

### MID-Grained

- **Nodes**: 16
- **Edges**: 18
- **Total Objects Represented**: 24
- **Average Degree**: 2.25
- **Graph Density**: 0.075

**Most Connected Nodes**:
- organism (degree: 12, objects: 3)
- artifact (degree: 3, objects: 4)
- person (degree: 3, objects: 2)
- commodity (degree: 3, objects: 2)
- illumination (degree: 2, objects: 1)

### COARSE-Grained

- **Nodes**: 6
- **Edges**: 7
- **Total Objects Represented**: 24
- **Average Degree**: 2.33
- **Graph Density**: 0.233

**Most Connected Nodes**:
- object (degree: 6, objects: 15)
- physical entity (degree: 3, objects: 5)
- skate park (degree: 2, objects: 1)
- state (degree: 1, objects: 1)
- group (degree: 1, objects: 1)

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
