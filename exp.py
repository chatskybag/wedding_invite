
"""
background-color: #f4f1ef;
"""

import os
from jinja2 import Template

# Список ваших изображений в нужном порядке
images = ["4.png", "5.png", "6.png"]
fill_link = "https://your-google-form-link.com"

html_template = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <link href="https://unpkg.com" rel="stylesheet">
<script src="https://unpkg.com"></script>
<script>AOS.init();</script>

<!-- Пример картинки -->
<img src="photo.jpg" data-aos="zoom-in" style="margin-left: 20%;">

</head>
<body>
    <div class="page-container">
        {% for img in images %}
    <img src="assets/{{ img }}" 
         data-aos="fade-up" 
         data-aos-duration="1000" 
         style="z-index: {{ loop.index }};" 
         alt="Page {{ loop.index }}">
        {% endfor %}
<script>
  AOS.init({
    once: false, // Анимация будет повторяться при скролле вверх и вниз
    mirror: true  // Элементы будут исчезать и снова появляться
  });
</script>


</body>
</html>
"""

template = Template(html_template)
with open("index_anim.html", "w", encoding="utf-8") as f:
    f.write(template.render(images=images, link=fill_link))

print("Сайт index.html успешно создан!")
