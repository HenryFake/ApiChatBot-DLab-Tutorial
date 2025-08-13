# Dlab Chat API

API pública temporal para pruebas de un chatbot con personalidad configurable.  
Puedes interactuar con ella enviando mensajes y manteniendo un hilo de conversación coherente.  

> ⚠️ Uso ilimitado por tiempo limitado, solo para pruebas.  
> Si encuentras fallos o quieres dar feedback, por favor escríbeme a **henrydevops6@gmail.com**.

---

## 📌 Endpoint
POST https://dlabot.azurewebsites.net/chat


---

## 📥 Ejemplo de solicitud

Envía un JSON con el rol del sistema, mensaje inicial del asistente y tu mensaje de usuario:

```json
{
    "sysApi": "Actúa como Goku",
    "assisApi": "Hola, soy Goku",
    "user_text": "¿Me enseñas algunas técnicas?"
}

```

## 📥 Ejemplo de respuesta
```json
{
    "content": "¡Muy bien! La Genkidama es una técnica poderosa que se basa en recolectar la energía..."
}
```

---

## 📥 Para mensajes con historial de memoria unicamente añadirlos a la lista
```json
{
  "sysApi": "Actúa como Goku",
  "assisApi": "Hola, soy Goku",
  "user_text": " Me enseñas algunas tecnicas?",
  "assisApi": "Claro el kamehamea o la gekidama?",
  "user_text": "Quiero el segundo"
}
```

---

## 🌐 Cómo probar con Thunder Client / Postman

**1. Configuración de la petición**
- **Método**: `POST`
- **URL**:  https://dlabot.azurewebsites.net/chat

**2. Encabezados**
- Content-Type: `application/json`

**3. Body (JSON)**

Ejemplo básico:
```json
{
  "sysApi": "Actúa como Goku",
  "assisApi": "Hola, soy Goku",
  "user_text": "¿Me enseñas algunas técnicas?"
}
```
**4. Respuesta esperada**


```json
{
    "content": "¡Muy bien! La Genkidama es una técnica poderosa que se basa en recolectar la energía...",
    "meta": {
        "author": "Henry C",
        "brand": "Dlab",
        "contact": {
            "email": "henrydevops6@gmail.com",
            "linkedin": "https://www.linkedin.com/in/henrycallupeancco/"
        },
        "version": "1.0.0"
    }
}
```



---

## 📬 Contacto

**Autor:** Henry C  
**Marca:** Dlab  

**Email:** henrydevops6@gmail.com  
**LinkedIn:** https://www.linkedin.com/in/henrycallupeancco/  

💡 Si pruebas la API y obtienes buenos resultados, me encantaría saber tu opinión.  
⚠️ Si detectas errores o comportamientos extraños, por favor notifícamelo para poder mejorar el servicio.

---


