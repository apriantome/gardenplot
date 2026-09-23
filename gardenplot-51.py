# === Stage 51: Add unit tests for search and filter behavior ===
# Project: GardenPlot
def test_search_and_filter():
    from garden import Garden

    g = Garden()
    g.add_bed("A1", "Tomatoes")
    g.add_bed("A2", "Lettuce")
    g.add_bed("B1", "Peppers")
    g.add_bed("B2", "Tomatoes")
    g.add_bed("C1", "Radishes")

    # search by name
    assert g.search("Tomato") == ["A1", "B2"]
    assert g.search("Pepper") == ["B1"]
    assert g.search("nonexistent") == []

    # filter by bed size category
    g.add_bed("D1", "Carrots")
    assert g.filter("large") == ["A1", "B2", "D1"]
    assert g.filter("small") == ["C1"]
    assert g.filter("medium") == ["A2", "B1"]

    # filter by harvest status
    g.mark_harvested("A1")
    g.mark_harvested("C1")
    assert g.filter("harvested") == ["A1", "C1"]
    assert g.filter("active") == ["A2", "B1", "B2", "D1"]

    # search combined with filter
    assert g.search("Tomato", filter_by="active") == ["B2"]
    assert g.search("Tomato", filter_by="harvested") == ["A1"]
    assert g.search("Tomato", filter_by="large") == ["A1", "B2"]
