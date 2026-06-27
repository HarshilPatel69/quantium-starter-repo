from dash.testing.application_runners import import_app


def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    header = dash_duo.find_element("#header")
    assert header.text == "Pink Morsel Sales Visualiser"


def test_visualisation_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    assert dash_duo.find_element("#sales-chart") is not None


def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-filter") is not None
