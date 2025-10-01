# Merged Multi-Granularity Scene Graph Report

## Image ID: 2331126

**Total Objects**: 19
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 19 | 15 | 1.27x |
| Mid | 19 | 14 | 1.36x |
| Coarse | 19 | 10 | 1.90x |

---

## Fine-Grained Merged Nodes

**Node Count**: 15

### black bowl
- **Merged Objects**: 1
- **Original Objects**: black bowl
- **Merged BBox**: x=328, y=107, w=36, h=19

### cat
- **Merged Objects**: 2
- **Original Objects**: cat, cat
- **Merged BBox**: x=116, y=184, w=168, h=96

### chair
- **Merged Objects**: 2
- **Original Objects**: chair, chair
- **Merged BBox**: x=30, y=109, w=438, h=351

### ear
- **Merged Objects**: 1
- **Original Objects**: ear
- **Merged BBox**: x=216, y=183, w=17, h=20

### eye
- **Merged Objects**: 1
- **Original Objects**: eye
- **Merged BBox**: x=234, y=225, w=15, h=10

### hardwood floor
- **Merged Objects**: 1
- **Original Objects**: hardwood floor
- **Merged BBox**: x=436, y=322, w=32, h=130

### lamp
- **Merged Objects**: 2
- **Original Objects**: lamp, lamp
- **Merged BBox**: x=192, y=36, w=98, h=106

### nose
- **Merged Objects**: 1
- **Original Objects**: nose
- **Merged BBox**: x=247, y=245, w=18, h=15

### pillow
- **Merged Objects**: 2
- **Original Objects**: pillow, pillow
- **Merged BBox**: x=42, y=250, w=335, h=121

### right ear
- **Merged Objects**: 1
- **Original Objects**: right ear
- **Merged BBox**: x=259, y=180, w=25, h=25

### table
- **Merged Objects**: 1
- **Original Objects**: table
- **Merged BBox**: x=192, y=122, w=191, h=60

### table lamp
- **Merged Objects**: 1
- **Original Objects**: table lamp
- **Merged BBox**: x=215, y=35, w=63, h=98

### wall
- **Merged Objects**: 1
- **Original Objects**: wall
- **Merged BBox**: x=30, y=35, w=358, h=152

### whiskers
- **Merged Objects**: 1
- **Original Objects**: whiskers
- **Merged BBox**: x=215, y=246, w=28, h=21

### white surfboard
- **Merged Objects**: 1
- **Original Objects**: white surfboard
- **Merged BBox**: x=291, y=80, w=23, h=45

---

## Mid-Grained Merged Nodes

**Node Count**: 14

### array
- **Merged Objects**: 1
- **Original Objects**: table
- **Merged BBox**: x=192, y=122, w=191, h=60

### black bowl
- **Merged Objects**: 1
- **Original Objects**: black bowl
- **Merged BBox**: x=328, y=107, w=36, h=19

### chemoreceptor
- **Merged Objects**: 1
- **Original Objects**: nose
- **Merged BBox**: x=247, y=245, w=18, h=15

### cushion
- **Merged Objects**: 2
- **Original Objects**: pillow, pillow
- **Merged BBox**: x=42, y=250, w=335, h=121

### facial hair
- **Merged Objects**: 1
- **Original Objects**: whiskers
- **Merged BBox**: x=215, y=246, w=28, h=21

### feline
- **Merged Objects**: 2
- **Original Objects**: cat, cat
- **Merged BBox**: x=116, y=184, w=168, h=96

### hardwood floor
- **Merged Objects**: 1
- **Original Objects**: hardwood floor
- **Merged BBox**: x=436, y=322, w=32, h=130

### partition
- **Merged Objects**: 1
- **Original Objects**: wall
- **Merged BBox**: x=30, y=35, w=358, h=152

### right ear
- **Merged Objects**: 1
- **Original Objects**: right ear
- **Merged BBox**: x=259, y=180, w=25, h=25

### seat
- **Merged Objects**: 2
- **Original Objects**: chair, chair
- **Merged BBox**: x=30, y=109, w=438, h=351

### sense organ
- **Merged Objects**: 2
- **Original Objects**: ear, eye
- **Merged BBox**: x=216, y=183, w=33, h=52

### source of illumination
- **Merged Objects**: 2
- **Original Objects**: lamp, lamp
- **Merged BBox**: x=192, y=36, w=98, h=106

### table lamp
- **Merged Objects**: 1
- **Original Objects**: table lamp
- **Merged BBox**: x=215, y=35, w=63, h=98

### white surfboard
- **Merged Objects**: 1
- **Original Objects**: white surfboard
- **Merged BBox**: x=291, y=80, w=23, h=45

---

## Coarse-Grained Merged Nodes

**Node Count**: 10

### array
- **Merged Objects**: 1
- **Original Objects**: table
- **Merged BBox**: x=192, y=122, w=191, h=60

### artifact
- **Merged Objects**: 7
- **Original Objects**: pillow, chair, lamp, lamp, pillow, chair, wall
- **Merged BBox**: x=30, y=35, w=438, h=425

### black bowl
- **Merged Objects**: 1
- **Original Objects**: black bowl
- **Merged BBox**: x=328, y=107, w=36, h=19

### body part
- **Merged Objects**: 3
- **Original Objects**: ear, nose, eye
- **Merged BBox**: x=216, y=183, w=49, h=77

### hardwood floor
- **Merged Objects**: 1
- **Original Objects**: hardwood floor
- **Merged BBox**: x=436, y=322, w=32, h=130

### living thing
- **Merged Objects**: 2
- **Original Objects**: cat, cat
- **Merged BBox**: x=116, y=184, w=168, h=96

### natural object
- **Merged Objects**: 1
- **Original Objects**: whiskers
- **Merged BBox**: x=215, y=246, w=28, h=21

### right ear
- **Merged Objects**: 1
- **Original Objects**: right ear
- **Merged BBox**: x=259, y=180, w=25, h=25

### table lamp
- **Merged Objects**: 1
- **Original Objects**: table lamp
- **Merged BBox**: x=215, y=35, w=63, h=98

### white surfboard
- **Merged Objects**: 1
- **Original Objects**: white surfboard
- **Merged BBox**: x=291, y=80, w=23, h=45

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v5/sample_2331126
