import plotly.express as px
data = dict(
    character=[
        "C",
        "Arhivos de programa",
        "Archivos de programa x86",
        "Usuarios",
        "Windows",
        "Usuario1",
        "Usuario2",
        "Escritorio",
        "Documentos"
        ],
    parent=["", "C", "C", "C", "C","Usuarios","Usuarios","Usuario1","Usuario1"],
    value=[0,25,25,25,25,10,10,2,4])

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
)
fig.show()
