preguntas_basicas = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es el ave nacional de Chile, reconocida por su gran envergadura y presencia en la Cordillera de los Andes?'],
        'alternativas': [
            ['Cóndor andino', 1],
            ['Águila mora', 0],
            ['Tucúquere', 0],
            ['Carancho', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Qué ave chilena es conocida por su pecho rojo brillante y su canto melodioso?'],
        'alternativas': [
            ['Loica', 1],
            ['Zorzal', 0],
            ['Diucón', 0],
            ['Chincol', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Cuál de estas aves es común en áreas urbanas chilenas y se caracteriza por su canto repetitivo y presencia en parques?'],
        'alternativas': [
            ['Tórtola común', 1],
            ['Gaviota dominicana', 0],
            ['Cachudito', 0],
            ['Peuco', 0]
        ]
    }
}

preguntas_intermedias = {
    'pregunta_1': {
        'enunciado': ['¿Qué ave chilena, de hábitos nocturnos, es reconocida por su canto que suena como "tucú-quere"?'],
        'alternativas': [
            ['Tucúquere', 1],
            ['Lechuza blanca', 0],
            ['Pequén', 0],
            ['Chuncho', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Cuál es el nombre del ave chilena que construye su nido en el suelo y es conocida por su comportamiento territorial y ruidoso?'],
        'alternativas': [
            ['Queltehue', 1],
            ['Tagua común', 0],
            ['Perdiz chilena', 0],
            ['Pato cortacorrientes', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Qué ave endémica de Chile se encuentra únicamente en la isla Robinson Crusoe y está clasificada como casi amenazada?'],
        'alternativas': [
            ['Cachudito de Juan Fernández / Picaflor de Juan Fernández', 1],
            ['Rayadito de Más Afuera', 0],
            ['Pingüino de Humboldt', 0],
            ['Fardela blanca', 0]
        ]
    }
}


preguntas_avanzadas = {
    'pregunta_1': {
        'enunciado': ['¿Cuál es el ave chilena más amenazada, endémica de la isla Alejandro Selkirk y con una población estimada de 50 a 250 individuos maduros?'],
        'alternativas': [
            ['Rayadito de Más Afuera', 1],
            ['Cachudito de Juan Fernández / Picaflor de Juan Fernández', 0],
            ['Pingüino de Humboldt', 0],
            ['Tapaculo', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Qué ave chilena, de la familia de los tinámidos, es conocida por sus huevos de color chocolate brillante y su hábito de nidificar en el suelo?'],
        'alternativas': [
            ['Perdiz chilena', 1],
            ['Tagua común', 0],
            ['Pato juarjual', 0],
            ['Queltehue', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Cuál es el nombre del ave chilena que habita en la zona central del país, es muy terrestre y prácticamente no vuela?'],
        'alternativas': [
            ['Tapaculo', 1],
            ['Chincol', 0],
            ['Diucón', 0],
            ['Zorzal', 0]
        ]
    }
}


pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}