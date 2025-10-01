# Merged Multi-Granularity Scene Graph Report

## Image ID: 2349422

**Total Objects**: 27
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 27 | 12 | 2.25x |
| Mid | 27 | 8 | 3.38x |
| Coarse | 27 | 9 | 3.00x |

---

## Fine-Grained Merged Nodes

**Node Count**: 12

### blue sky
- **Merged Objects**: 2
- **Original Objects**: blue sky, blue sky
- **Merged BBox**: x=0, y=0, w=498, h=332

### clouds
- **Merged Objects**: 2
- **Original Objects**: clouds, clouds
- **Merged BBox**: x=181, y=10, w=318, h=109

### eyebrow
- **Merged Objects**: 2
- **Original Objects**: eyebrow, eyebrow
- **Merged BBox**: x=135, y=94, w=68, h=35

### hair
- **Merged Objects**: 1
- **Original Objects**: hair
- **Merged BBox**: x=97, y=86, w=21, h=15

### hand
- **Merged Objects**: 1
- **Original Objects**: hand
- **Merged BBox**: x=295, y=283, w=74, h=48

### he
- **Merged Objects**: 1
- **Original Objects**: he
- **Merged BBox**: x=1, y=48, w=358, h=283

### head
- **Merged Objects**: 1
- **Original Objects**: head
- **Merged BBox**: x=78, y=35, w=171, h=190

### kite
- **Merged Objects**: 7
- **Original Objects**: kite, kite, kite, kite, kite, kite, kite
- **Merged BBox**: x=198, y=157, w=107, h=128

### man
- **Merged Objects**: 1
- **Original Objects**: man
- **Merged BBox**: x=0, y=62, w=360, h=267

### shirt
- **Merged Objects**: 1
- **Original Objects**: shirt
- **Merged BBox**: x=4, y=144, w=302, h=186

### sky
- **Merged Objects**: 6
- **Original Objects**: sky, sky, sky, sky, sky, sky
- **Merged BBox**: x=2, y=2, w=495, h=330

### string
- **Merged Objects**: 2
- **Original Objects**: string, string
- **Merged BBox**: x=210, y=157, w=102, h=132

---

## Mid-Grained Merged Nodes

**Node Count**: 8

### blue sky
- **Merged Objects**: 2
- **Original Objects**: blue sky, blue sky
- **Merged BBox**: x=0, y=0, w=498, h=332

### body_part
- **Merged Objects**: 2
- **Original Objects**: head, hand
- **Merged BBox**: x=78, y=35, w=291, h=296

### clothing
- **Merged Objects**: 1
- **Original Objects**: shirt
- **Merged BBox**: x=4, y=144, w=302, h=186

### cord
- **Merged Objects**: 2
- **Original Objects**: string, string
- **Merged BBox**: x=210, y=157, w=102, h=132

### material
- **Merged Objects**: 1
- **Original Objects**: he
- **Merged BBox**: x=1, y=48, w=358, h=283

### nature
- **Merged Objects**: 11
- **Original Objects**: sky, eyebrow, eyebrow, hair, sky, clouds, sky, sky, clouds, sky (+1 more)
- **Merged BBox**: x=2, y=2, w=497, h=330

### person
- **Merged Objects**: 1
- **Original Objects**: man
- **Merged BBox**: x=0, y=62, w=360, h=267

### text
- **Merged Objects**: 7
- **Original Objects**: kite, kite, kite, kite, kite, kite, kite
- **Merged BBox**: x=198, y=157, w=107, h=128

---

## Coarse-Grained Merged Nodes

**Node Count**: 9

### artifact
- **Merged Objects**: 3
- **Original Objects**: string, string, shirt
- **Merged BBox**: x=4, y=144, w=308, h=186

### blue sky
- **Merged Objects**: 2
- **Original Objects**: blue sky, blue sky
- **Merged BBox**: x=0, y=0, w=498, h=332

### body part
- **Merged Objects**: 2
- **Original Objects**: head, hand
- **Merged BBox**: x=78, y=35, w=291, h=296

### gas
- **Merged Objects**: 6
- **Original Objects**: sky, sky, sky, sky, sky, sky
- **Merged BBox**: x=2, y=2, w=495, h=330

### living thing
- **Merged Objects**: 1
- **Original Objects**: man
- **Merged BBox**: x=0, y=62, w=360, h=267

### natural object
- **Merged Objects**: 3
- **Original Objects**: eyebrow, eyebrow, hair
- **Merged BBox**: x=97, y=86, w=106, h=43

### natural phenomenon
- **Merged Objects**: 2
- **Original Objects**: clouds, clouds
- **Merged BBox**: x=181, y=10, w=318, h=109

### substance
- **Merged Objects**: 1
- **Original Objects**: he
- **Merged BBox**: x=1, y=48, w=358, h=283

### writing
- **Merged Objects**: 7
- **Original Objects**: kite, kite, kite, kite, kite, kite, kite
- **Merged BBox**: x=198, y=157, w=107, h=128

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v6.1/sample_2349422
