import json
import pyttsx3
import speech_recognition as sr

preguntas ={'pregunta1': 'TIENE FRECUENTES DOLORES DE CABEZA','pregunta2': 'TIENE MAL APETITO',
            'pregunta3': 'DUERME MAL',  'pregunta4':'SE ASUSTA CON FACILIDAD','pregunta5':'SUFRE DE TEMBLOR DE MANOS',
            'pregunta6':'SE SIENTE NERVIOSO(A) O TENSO(A)','pregunta7':'SUFRE DE MALA DIGESTIÓN',
            'pregunta8':'ES INCAPAZ DE PENSAR CON CLARIDAD',  'pregunta9':'SE SIENTE TRISTE',
            'pregunta10':'LLORA CON MUCHA FRECUENCIA', 'pregunta11': 'TIENE DIFICULTAD PARA DISFRUTAR SUS ACTIVIDADES DIARIAS',
            'pregunta12':'TIENE DIFICULTAD PARA TOMAR DECISIONES', 'pregunta13':'TIENE DIFICULTAD PARA HACER SU TRABAJO, SU TRABAJO SE HA VISTO AFECTADO',
            'pregunta14': 'ES INCAPAZ DE DESEMPEÑAR UN PAPEL ÚTIL EN SU VIDA', 'pregunta15': 'HA PERDIDO INTERES EN LAS COSAS',
            'pregunta16': 'SE SIENTE ABURRIDO','pregunta17':'HA TENIDO LA IDEA DE ACABAR CON SU VIDA',
            'pregunta18': 'SE SIENTE CANSADO TODO EL TIEMPO', 'pregunta19':'SIENTE UD. QUE ALGUIEN HA TRATADO DE HERIRLE DE ALGUNA FORMA',
            'pregunta20': 'ES UD. UNA PERSONA MUCHO MAS IMPORTANTE DE LO QUE PIENSAN LOS DEMÁS',
            'pregunta21': 'HA NOTADO INTERFERENCIA O ALGO RARO EN SUS PENSAMIENTOS',
            'pregunta22': 'OYE VOCES SIN SABER DE DÓNDE VIENEN, O QUE OTRAS PERSONAS NO PUEDEN OÍRLAS',
            'pregunta23': 'HA TENIDO CONVULSIONES, ATAQUES O CAÍDAS AL SUELO, CON MOVIMIENTOS DE BRAZOS Y PIERNAS, CON MORDEDURA DE LA LENGUA O PÉRDIDA DE CONOCIMIENTO',
            'pregunta24': 'ALGUNA VEZ LE HA PARECIDO A SU FAMILIA, SUS AMIGOS, SU MEDICO O SU SACERDOTE QUE ESTABA BEBIENDO DEMASIADO',
            'pregunta25': 'ALGUNA VEZ HA QUERIDO DEJAR DE BEBER, PERO NO HA PODIDO',
            'pregunta26': 'HA TENIDO ALGUNA VEZ DIFICULTADES EN EL TRABAJO O ESTUDIO A CAUSA DE LA BEBIDA, COMO BEBER EN EL TRABAJO O LUGAR DE ESTUDIO O FALTAR A ELLOS',
            'pregunta27': 'HA ESTADO EN RIÑAS O LE HAN DETENIDO ESTANDO BORRACHO', 
            'pregunta28': 'LE HA PARECIDO ALGUNA VEZ QUE HA BEBIDO DEMASIADO'
            }
#SPEECHRECOGNITION 
r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=1)


#SINTETIZADOR DE VOZ 
engine = pyttsx3.init()
engine.setProperty('rate', '146')
engine.setProperty('voice', 'spanish')

def habla(texto):
    engine.say(texto)
    engine.runAndWait()
    
    
    
#data= json.dumps(preguntas, ensure_ascii=False)
print()
print("--------TEST DE DESPISTAJE--------")
habla("HOLA SO")

habla("COMENZEMOS REALIZAR DESPISTAJE PSICOLOGICO")


res=[]
s=int()
for i in preguntas:
    habla(preguntas[i])
    with mic as source:
        r.adjust_for_ambient_noise(source) # Calibración si el audio tiene ruido de fondo
        audio = r.listen(source)
    voz =r.recognize_google(audio, language='es-PE')
    print(voz)
    respuesta=input(" " +preguntas[i]+':')
    
    if respuesta =='si' or respuesta=='no':
        res.append(respuesta)
    else:
          print("Las respuestas solo pueden ser (si o no)")
psi=0
pno=0
print()
for i in res:
    if i=='si':
        psi+=1
    elif i=='no':
        pno+=1
print(">>DIAGNOSTICO:")
if psi <=7:
    print("Normal" )    
elif psi >=8 or psi <=14 :
    print("Leve")
elif psi >=14 or psi <=18 :
    print("Moderado")
elif psi >=19 or psi <=22 :
    print("Severo")
elif psi >=23 :
    print("Muy severo")
    
print(res)
print(psi)
print(pno)
    
