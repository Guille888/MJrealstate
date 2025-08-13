
import graphviz

# Crear un objeto de gráfico dirigido
dot = graphviz.Digraph('Flujograma', comment='Modelo de Mejora Continua')

# Configurar el formato
dot.attr(rankdir='LR', size='12,6', dpi='300')
dot.attr('node', shape='box', style='filled', fontname='Arial')

# Añadir nodos con diferentes formas y colores
dot.node('Inicio', 'Inicio', shape='oval', fillcolor='lightblue')
dot.node('Analizar', 'Analizar', fillcolor='lightgreen')
dot.node('Comunicar', 'Comunicar', fillcolor='lightcoral')
dot.node('Decidir', 'Decidir', shape='diamond', fillcolor='lightyellow')
dot.node('Implementar', 'Implementar', fillcolor='lightpink')
dot.node('Medir', 'Medir', fillcolor='lightgrey')
dot.node('Fin', 'Fin', shape='oval', fillcolor='lightblue')

# Añadir conexiones con etiquetas
dot.edge('Inicio', 'Analizar')
dot.edge('Analizar', 'Comunicar')
dot.edge('Comunicar', 'Decidir')
dot.edge('Decidir', 'Implementar', label='Aprobado')
dot.edge('Implementar', 'Medir')
dot.edge('Medir', 'Analizar', label='Ciclo continuo')
dot.edge('Medir', 'Fin', label='Proceso completado')

# Renderizar y guardar el gráfico
dot.render('flujograma_mejora_continua', format='png', cleanup=True)
