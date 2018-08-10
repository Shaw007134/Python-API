import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style = LCS)

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['awesome-python','public-apis','system-design-primer']

plot_dicts = [
	{'value': 53651, 'label': 'Collection of the python lib and tools'},
	{'value': 40983, 'label': 'Public apis of Python'},
	{'value': 40689, 'label': 'About the systme design'},
	]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')


