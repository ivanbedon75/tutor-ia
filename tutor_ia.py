#!/usr/bin/env python
# coding: utf-8

# In[4]:


# tutor_ia.py

def generar_respuesta_tutor(prompt_usuario):
    """
    Procesa la entrada del usuario como tutor universitario experto en pedagogía.
    """
    # Introducción motivadora
    introduccion = (
        "¡Excelente decisión al abordar este tema! Reconocer tus dudas y plantearlas "
        "es un paso crucial en el aprendizaje autónomo. Tu interés demuestra compromiso "
        "y voluntad de crecer académicamente."
    )

    # Explicación pedagógica (puede personalizarse más con NLP o IA externa)
    explicacion = (
        "En relación a tu pregunta, es fundamental entender que... [Explicación clara del tema]. "
        "Un ejemplo puede ayudar: imagina que... [Ejemplo aplicado]. Este enfoque permite comprender mejor los fundamentos del tema."
    )

    # Actividad complementaria sugerida
    actividad = {
        "nombre": "Aplicación del concepto en contexto real",
        "instrucciones": "Redacta un caso práctico donde apliques el concepto abordado, detallando los pasos seguidos y justificando tus decisiones.",
        "objetivo": "Reforzar la comprensión aplicando el conocimiento a un caso real.",
        "temas_recomendados": [
            "Aprendizaje significativo en ambientes virtuales",
            "Autores como David Ausubel o Lev Vygotsky",
            "Términos de búsqueda: 'formative feedback in higher education', 'virtual tutoring strategies'"
        ]
    }

    # Evaluación de la respuesta del usuario (simulada para ejemplo)
    evaluacion = {
        "fortalezas": [
            "Buena comprensión del concepto.",
            "Uso adecuado del lenguaje académico."
        ],
        "areas_mejora": [
            "Profundizar en el marco teórico.",
            "Agregar ejemplos propios para evidenciar comprensión."
        ],
        "sugerencias": [
            "Consultar fuentes académicas en Google Scholar sobre el tema.",
            "Desarrollar un esquema o mapa conceptual."
        ],
        "nota": 8  # Puedes modificarlo según análisis IA
    }

    # Resultado y rúbrica
    if evaluacion["nota"] >= 7:
        resultado = (
            "¡Muy bien hecho! Has demostrado un nivel adecuado de comprensión.\n"
            "Sigue así, tu esfuerzo vale la pena. Recuerda que aprender es un proceso continuo y progresivo."
        )
    else:
        resultado = (
            "Es importante reforzar algunos aspectos antes de avanzar.\n"
            "Te propongo otra actividad relacionada para consolidar tus conocimientos."
        )

    rubrica = {
        "Claridad conceptual": 3,
        "Aplicación práctica": 2,
        "Uso de fuentes académicas": 2,
        "Reflexión crítica": 3,
        "Total (sobre 10)": evaluacion["nota"]
    }

    # Construcción de la respuesta final
    respuesta = f"""
**TUTOR-IA: Retroalimentación Formativa**

**Introducción motivadora**
{introduccion}

**Explicación pedagógica**
{explicacion}

**Actividad complementaria sugerida**
• Nombre: {actividad['nombre']}
• Instrucciones: {actividad['instrucciones']}
• Objetivo: {actividad['objetivo']}
• Recomendaciones de lectura:
    - {actividad['temas_recomendados'][0]}
    - {actividad['temas_recomendados'][1]}
    - {actividad['temas_recomendados'][2]}

**Evaluación de la respuesta**
• Fortalezas:
  - {chr(10).join(evaluacion['fortalezas'])}
• Áreas de mejora:
  - {chr(10).join(evaluacion['areas_mejora'])}
• Sugerencias:
  - {chr(10).join(evaluacion['sugerencias'])}

**Resultado**
{resultado}

**Rúbrica de evaluación**
{chr(10).join([f"- {k}: {v}" for k, v in rubrica.items()])}
"""
    return respuesta

# Ejemplo de uso en JupyterLab:
if __name__ == "__main__":
    pregunta_usuario = input("Ingresa tu pregunta o tema de estudio: ")
    print(generar_respuesta_tutor(pregunta_usuario))

# In[ ]:




