import numpy as np
from tensorflow.keras.models import Model,load_model
from tensorflow.keras.layers import Input, Dense, multiply
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

def paisPrimeraDivisionEsp(eleccionpais):
    metric = np.array([
    [14], [26], [19], [15], [7], [25], [3], [25], [25], [3], [20], [10], 
            [19], [20], [27], [7], [5], [25], [5], [2], [13], [7], [4], [25], 
            [24], [25], [3], [26], [12], [20], [26], [25], [8], [23],  [14], 
            [17], [7], [7], [26], [16], [9], [3], [26], [22], [7], [14], [25], 
            [15], [7], [6], [1], [14], [20], [8], [21], [25], [18], [28], [11], [20]
    ])

    labels = np.array([
        1, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 2, 1, 4, 2, 1, 1, 1, 3, 1, 2, 2, 1, 2, 
        1, 1, 0, 1, 0, 0, 2, 2, 1,  1, 4, 2, 2, 0, 0, 3, 1, 2, 2, 3, 3, 0, 0, 2, 
        2, 2, 1, 0, 1, 2, 0, 2, 1, 2, 1
    ])

    # Convertir etiquetas a categorías
    labels = to_categorical(labels, num_classes=5)
    print(labels)
    metric_train, metric_test, labels_train, labels_test = train_test_split(metric, labels, test_size=0.2, random_state=42)
    model_path = 'modelo_primera_division.h5'
    try:
        model = load_model(model_path)
        print("Modelo cargado desde el disco.")
    except:
        print("Entrenando un nuevo modelo...")
        seo_input = Input(shape=(metric.shape[1],), name='seo_input')
        dense_1 = Dense(64, activation='relu')(seo_input)
        dense_2 = Dense(64, activation='relu')(dense_1)
        output = Dense(5, activation='softmax')(dense_2)

        model = Model(inputs=seo_input, outputs=output)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Entrenar el modelo
        #model.fit(metric_train, labels_train, epochs=9000, batch_size=2, verbose=1)
        model.fit(metric, labels, epochs=9000, batch_size=2)
        model.save(model_path)
    loss, accuracy = model.evaluate(metric_test, labels_test, verbose=0)
    print(f"Precisión del modelo en los datos de prueba: {accuracy:.2f}{loss}")
        
        # Predicción
    new_metrics = np.array([[eleccionpais]])  # Asegurar que sea 2D
    pred1 = model.predict(new_metrics)
    print(pred1)

    data=pred1[0]
    liga=0

    data=pred1[0]
    max_valor=np.max(data)
    liga=np.argmax(data)
    print(liga)
    return liga


def paisSegundaDivisionEsp(eleccion_pais):
    metric = np.array([
    [14], [26], [19], [15], [7], [25], [3], [25], [25], [3], [20], [10], 
            [19], [20], [27], [7], [5], [25], [5], [2], [13], [7], [4],[25], 
            [24], [25], [3], [26], [12], [20], [26], [25], [8], [23], [3], [14], 
            [17], [7], [7], [26], [16], [9], [3], [26], [22], [7], [25], 
            [15], [7], [6], [1], [14], [20], [8], [21], [25], [18], [28], [11], [20]
    ])

    labels = np.array([
        0, 1, 2, 1, 3, 1, 1, 0, 0, 1, 0, 2, 1, 0, 3, 2, 1, 1, 0, 3, 0, 3, 3, 0, 0, 0, 1, 1, 3, 1, 4, 0, 2, 0, 2, 0, 3, 3, 2, 1, 4, 3, 0, 0, 3, 3, 0, 1, 2, 2, 1, 2, 0, 0, 2, 1, 2, 0, 3, 1

    ])

    # Convertir etiquetas a categorías
    labels = to_categorical(labels, num_classes=5)
    print(metric.shape[1])
    model_path = 'modelo_segunda2_division.h5'
    try:
        model = load_model(model_path)
        print("Modelo cargado desde el disco.")
    # Construir el modelo
    except:
        seo_input = Input(shape=(metric.shape[1],), name='seo_input')
        dense_1 = Dense(64, activation='relu')(seo_input)
        dense_2 = Dense(64, activation='relu')(dense_1)
        output = Dense(5, activation='softmax')(dense_2)

        model = Model(inputs=seo_input, outputs=output)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Entrenar el modelo
        model.fit(metric, labels, epochs=9900, batch_size=2)
        model.save(model_path)
    
    # Predicción
    new_metrics = np.array([[eleccion_pais]])  # Asegurar que sea 2D
    pred1 = model.predict(new_metrics)
    print(pred1)

    data=pred1[0]
    max_valor=np.max(data)
    liga=np.argmax(data)
    print(liga)
    return liga

def paisTerceraDivisionEsp(eleccion_pais):
    metric = np.array([
    [14], [26], [19], [15], [7], [25], [3], [25], [25], [3], [20], [10], 
            [19],[20] , [27], [7], [5], [25], [5], [2], [13], [7], [4], [25], 
            [24], [25], [3], [26], [20], [26], [25], [8], [23], [14], 
            [17], [7], [7], [26], [16], [3], [26], [22], [7], [25], 
            [15], [7], [6], [1], [14], [20], [8], [21], [25], [18], [28], [11], [20]
    ])

    labels = np.array([4, 2, 4, 2, 4, 2, 2, 3, 2, 2, 4, 4, 1, 4, 4, 4, 2, 3, 4, 4, 3, 4, 4, 3, 2, 3, 2, 1, 4, 0, 3, 4, 3, 4, 4, 4, 4, 2, 4, 3, 2, 4, 4, 3, 3, 4, 4, 4, 4, 3, 2, 4, 2, 4, 4, 4, 2]
        

    )

    # Convertir etiquetas a categorías
    labels = to_categorical(labels, num_classes=5)
    metric_train, metric_test, labels_train, labels_test = train_test_split(metric, labels, test_size=0.2, random_state=42)
    print(metric.shape[1])
    model_path = 'modelo_tercera_division.h5'
    try:
        model = load_model(model_path)
        print("Modelo cargado desde el disco.")
    # Construir el modelo
    except:
        seo_input = Input(shape=(metric.shape[1],), name='seo_input')
        dense_1 = Dense(128, activation='relu')(seo_input)
        dense_2 = Dense(128, activation='relu')(dense_1)
        output = Dense(5, activation='softmax')(dense_2)

        model = Model(inputs=seo_input, outputs=output)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Entrenar el modelo
        model.fit(metric, labels, epochs=9000, batch_size=2)
        model.save(model_path)
    loss, accuracy = model.evaluate(metric_test, labels_test, verbose=0)
    print(f"Precisión del modelo en los datos de prueba: {accuracy:.2f}{loss}")
    
    # Predicción
    new_metrics = np.array([[eleccion_pais]])  # Asegurar que sea 2D
    pred1 = model.predict(new_metrics)
    print(pred1)

    data=pred1[0]
    max_valor=np.max(data)
    liga=np.argmax(data)
    print(liga)
    return liga

listDivision=[]
def ligaPaisPrimera(liga,ligaDestino):
    ligas = np.array([
        [1], [0], [2], [0], [2], [0], [0], [0], [2], [0], [0], [2], [2], [1], [4], [2], [1], [1], [1], [3], [1], [2], [2], [1], [2], [1], [1], [0], [1], [0], [0], [2], [2], [1], [3], [1], [4], [2], [2], [0], [0], [3], [1], [2], [2], [3], [3], [0], [0], [2], [2], [2], [1], [0], [1], [2], [0], [2], [1], [2], [1]

    ])

    paises = np.array([
    13, 25, 18, 14, 6, 24, 2, 24, 24, 2, 19, 9, 18, 19, 26, 6, 4, 24, 4, 1, 12, 6, 3, 24, 23, 24, 2, 25, 11, 19, 25, 24, 7, 22, 2, 13, 16, 6, 6, 25, 15, 8, 2, 25, 21, 6, 13, 24, 14, 6, 5, 0, 13, 19, 7, 20, 24, 17, 27, 10, 19
    ])

    # Convertir etiquetas a categorías
    paises = to_categorical(paises, num_classes=28)
    print(paises.shape[1])
    model_path = 'modelo_primera_liga.h5'
    try:
        model2 = load_model(model_path)
        print("Modelo cargado desde el disco.")
    # Construir el modelo
    except:

    # Construir el modelo
        seo_input2 = Input(shape=(ligas.shape[1],), name='seo_input')
        dense_12 = Dense(560, activation='relu')(seo_input2)
        attention = Dense(560, activation='softmax', name='attention_weights')(dense_12)
        attention_output = multiply([dense_12, attention], name='attention_applied')
        dense_22 = Dense(560, activation='relu')(attention_output)
    
        dense_32 = Dense(560, activation='relu')(dense_22)

        dense_42 = Dense(560, activation='relu')(dense_32)
    

        output2 = Dense(28, activation='softmax')(dense_42)
        model2 = Model(inputs=seo_input2, outputs=output2)
        model2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Entrenar el modelo
        model2.fit(ligas, paises, epochs=6000, batch_size=5)
        model2.save(model_path)
    
   

    new_metrics2 = np.array([[liga]])  # Asegurar que sea 2D
    pred2 = model2.predict(new_metrics2)
    print("pred2")
    print(pred2)
    data2=pred2[0]
    print(data2)
    print(data2[ligaDestino-1])
    return data2[ligaDestino-1]


   
    
    

def ligaPaisSegunda(liga,ligaDestino):
    ligas = np.array([

[0], [1], [2], [1], [3], [1], [1], [0], [0], [1], [0], [2], [1], [0], [3], [2], [1], [1], [0], [3], [0], [3], [3], [0], [0], [0], [1], [1], [3], [1], [4], [0], [2], [0], [2], [0], [3], [3], [2], [1], [4], [3], [0], [0], [3], [3], [0], [1], [2], [2], [1], [2], [0], [0], [2], [1], [2], [0], [3], [1]





    ])

    paises = np.array([
    13, 25, 18, 14, 6, 24, 2, 24, 24, 2, 19, 9,
18, 19, 26, 6, 4, 24, 4, 1, 12, 6, 3, 24,
23, 24, 2, 25, 11, 19, 25, 24, 7, 22, 2, 13,
16, 6, 6, 25, 15, 8, 2, 25, 21, 6, 24,
14, 6, 5, 0, 13, 19, 7, 20, 24, 17, 27, 10, 
19
    ])

    # Convertir etiquetas a categorías
    paises = to_categorical(paises, num_classes=28)
    print(paises.shape[1])
    model_path = 'modelo_segunda_liga.h5'
    try:
        model2 = load_model(model_path)
        print("Modelo cargado desde el disco.")
    # Construir el modelo
    except:
    # Construir el modelo
        seo_input2 = Input(shape=(ligas.shape[1],), name='seo_input')
        dense_12 = Dense(560, activation='relu')(seo_input2)
        attention = Dense(560, activation='softmax', name='attention_weights')(dense_12)
        attention_output = multiply([dense_12, attention], name='attention_applied')
        dense_22 = Dense(560, activation='relu')(attention_output)
    
        dense_32 = Dense(560, activation='relu')(dense_22)

        dense_42 = Dense(560, activation='relu')(dense_32)
    
        output2 = Dense(28, activation='softmax')(dense_42)
        

        model2 = Model(inputs=seo_input2, outputs=output2)
        model2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Entrenar el modelo
        model2.fit(ligas, paises, epochs=6000, batch_size=5)
        model2.save(model_path)

    new_metrics2 = np.array([[liga]])  # Asegurar que sea 2D
    pred2 = model2.predict(new_metrics2)
    print(pred2)
    data2=pred2[0]

    
    
    return data2[ligaDestino-1]


def ligaPaisTercera(liga,ligaDestino):
    ligas = np.array([


[4], [2], [4], [2], [4], [2], [2], [3], [2], [2], [4], [4], [1], [4], [4], 
    [4], [2], [3], [4], [4], [3], [4], [4], [3], [2], [3], [2], [1], [4], [0], 
    [3], [4], [3], [4], [4], [4], [4], [2], [4], [3], [2], [4], [4], [3], [3], 
    [4], [4], [4], [4], [3], [2], [4], [2], [4], [4], [4], [2]




    ])

    paises = np.array([
     13, 25, 18, 14, 6, 24, 2, 24, 24, 2, 19, 9,
18, 19, 26, 6, 4, 24, 4, 1, 12, 6, 3, 24,
23, 24, 2, 25, 19, 25, 24, 7, 22, 13,
16, 6, 6, 25, 15, 2, 25, 21, 6, 24,
14, 6, 5, 0, 13, 19, 7, 20, 24, 17, 27, 10,
19
    ])

    # Convertir etiquetas a categorías
    paises = to_categorical(paises, num_classes=28)
    print(paises.shape[1])
    ligas_train, ligas_test, paises_train, paises_test = train_test_split(ligas, paises, test_size=0.2, random_state=42)
    # Construir el modelo
    model_path = 'modelo_tercera_liga.h5'
    try:
        model2 = load_model(model_path)
        print("Modelo cargado desde el disco.")
    # Construir el modelo
    except:
        seo_input2 = Input(shape=(ligas.shape[1],), name='seo_input')
        dense_12 = Dense(560, activation='relu')(seo_input2)
        attention = Dense(560, activation='softmax', name='attention_weights')(dense_12)
        attention_output = multiply([dense_12, attention], name='attention_applied')
        dense_22 = Dense(560, activation='relu')(attention_output)
    
        dense_32 = Dense(560, activation='relu')(dense_22)

        dense_42 = Dense(560, activation='relu')(dense_32)
    
        output2 = Dense(28, activation='softmax')(dense_42)

        model2 = Model(inputs=seo_input2, outputs=output2)
        model2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Entrenar el modelo
        model2.fit(ligas, paises, epochs=6000, batch_size=2)
        model2.save(model_path)
    loss, accuracy = model2.evaluate(ligas_test, paises_test, verbose=0)
    print(f"Precisión del modelo en los datos de prueba: {accuracy:.2f}{loss}")

    new_metrics2 = np.array([[liga]])  # Asegurar que sea 2D
    pred2 = model2.predict(new_metrics2)
    print(pred2)
    data2=pred2[0]

  
    
    return data2[ligaDestino-1]
def ligaUniversal(liga,ligaDestino):
    total=[[0, 0, 13], [0, 1, 25], [0, 2, 18], [0, 1, 14], [0, 3, 6], [0, 1, 24], [0, 1, 2], [0, 0, 24], [0, 0, 24], [0, 1, 2], [0, 0, 19], [0, 2, 9],
[0, 1, 18], [0, 0, 19], [0, 3, 26], [0, 2, 6], [0, 1, 4], [0, 0, 24], [0, 0, 4], [0, 3, 1], [0, 0, 12], [0, 3, 6], [0, 3, 3], [0, 0, 24],
[0, 0, 23], [0, 0, 24], [0, 1, 2], [0, 1, 25], [0, 3, 11], [0, 1, 19], [0, 1, 25], [0, 0, 24], [0, 2, 7], [0, 0, 22], [0, 2, 2], [0, 0, 13],
[0, 2, 16], [0, 0, 6], [0, 0, 6], [0, 1, 25], [0, 2, 15], [0, 0, 8], [0, 2, 2], [0, 1, 25], [0, 4, 21], [0, 3, 6], [0, 0, 24],
[0, 0, 14], [0, 3, 6], [0, 2, 5], [0, 0, 0], [0, 3, 13], [0, 1, 19], [0, 0, 7], [0, 0, 20], [0, 3, 24], [0, 0, 17], [0, 0, 27], [0, 1, 10],
[0, 1, 19],
[1, 0, 13], [1, 1, 25], [1, 2, 18], [1, 1, 14], [1, 3, 6], [1, 1, 24], [1, 1, 2], [1, 0, 24], [1, 0, 24], [1, 1, 2], [1, 0, 19], [1, 2, 9],
[1, 1, 18], [1, 0, 19], [1, 3, 26], [1, 2, 6], [1, 1, 4], [1, 0, 24], [1, 0, 4], [1, 3, 1], [1, 0, 12], [1, 3, 6], [1, 3, 3], [1, 0, 24],
[1, 0, 23], [1, 0, 24], [1, 1, 2], [1, 1, 25], [1, 3, 11], [1, 1, 19], [1, 1, 25], [1, 0, 24], [1, 2, 7], [1, 0, 22], [1, 2, 2], [1, 0, 13],
[1, 2, 16], [1, 0, 6], [1, 0, 6], [1, 1, 25], [1, 2, 15], [1, 0, 8], [1, 2, 2], [1, 1, 25], [1, 4, 21], [1, 3, 6], [1, 0, 24],
[1, 0, 14], [1, 3, 6], [1, 2, 5], [1, 0, 0], [1, 3, 13], [1, 1, 19], [1, 0, 7], [1, 0, 20], [1, 3, 24], [1, 0, 17], [1, 0, 27], [1, 1, 10],
[1, 1, 19],
[2, 4, 13], [2, 2, 25], [2, 4, 18], [2, 2, 14], [2, 4, 6], [2, 2, 24], [2, 2, 2], [2, 3, 24], [2, 2, 24], [2, 2, 2], [2, 2, 19], [2, 4, 9],
[2, 1, 18], [2, 4, 19], [2, 4, 26], [2, 2, 6], [2, 3, 4], [2, 4, 24], [2, 4, 4], [2, 1, 1], [2, 4, 12], [2, 3, 6], [2, 4, 3], [2, 3, 24],
[2, 2, 23], [2, 4, 24], [2, 2, 2], [2, 1, 25], [2, 4, 11], [2, 3, 19], [2, 4, 25], [2, 2, 24], [2, 4, 7], [2, 3, 22], [2, 2, 2], [2, 4, 13],
[2, 2, 16], [2, 3, 6], [2, 4, 6], [2, 2, 25], [2, 2, 15], [2, 0, 8], [2, 3, 2], [2, 1, 25], [2, 4, 21], [2, 3, 6], [2, 4, 24],
[2, 3, 14], [2, 4, 6], [2, 3, 5], [2, 0, 0], [2, 3, 13], [2, 4, 19], [2, 3, 7], [2, 4, 20], [2, 4, 24], [2, 3, 17], [2, 4, 27], [2, 0, 10],
[2, 3, 19]]
    ligas = np.array([ [0, 0], [0, 1], [0, 2], [0, 1], [0, 3], [0, 1], [0, 1], [0, 0], [0, 0], [0, 1], [0, 0], [0, 2], [0, 1], [0, 0], [0, 3], [0, 2], [0, 1], [0, 1], [0, 0], [0, 3], [0, 0], [0, 3], [0, 3], [0, 0], [0, 0], [0, 0], [0, 1], [0, 1], [0, 3], [0, 1], [0, 4], [0, 0], [0, 2], [0, 0], [0, 2], [0, 0], [0, 3], [0, 3], [0, 2], [0, 1], [0, 4], [0, 3], [0, 0], [0, 0], [0, 3], [0, 3], [0, 0], [0, 1], [0, 2], [0, 2], [0, 1], [0, 2], [0, 0], [0, 0], [0, 2], [0, 1], [0, 2], [0, 0], [0, 3], [0, 1], [0, 4], [1, 0], [1, 1], [1, 2], [1, 1], [1, 3], [1, 1], [1, 1], [1, 0], [1, 0], [1, 1], [1, 0], [1, 2], [1, 1], [1, 0], [1, 3], [1, 2], [1, 1], [1, 1], [1, 0], [1, 3], [1, 0], [1, 3], [1, 3], [1, 0], [1, 0], [1, 0], [1, 1], [1, 1], [1, 3], [1, 1], [1, 4], [1, 0], [1, 2], [1, 0], [1, 2], [1, 0], [1, 3], [1, 3], [1, 2], [1, 1], [1, 4], [1, 3], [1, 0], [1, 0], [1, 3], [1, 3], [1, 0], [1, 1], [1, 2], [1, 2], [1, 1], [1, 2], [1, 0], [1, 0], [1, 2], [1, 1], [1, 2], [1, 0], [1, 3], [1, 1],[2, 4], [2, 2], [2, 4], [2, 2], [2, 4], [2, 2], [2, 2], [2, 3], [2, 2], [2, 2],
    [2, 4], [2, 4], [2, 1], [2, 4], [2, 4], [2, 4], [2, 2], [2, 3], [2, 4], [2, 4],
    [2, 3], [2, 4], [2, 4], [2, 3], [2, 2], [2, 3], [2, 2], [2, 1], [2, 4], [2, 0],
    [2, 3], [2, 4], [2, 3], [2, 4], [2, 4], [2, 4], [2, 4], [2, 2], [2, 4], [2, 3],
    [2, 2], [2, 4], [2, 4], [2, 3], [2, 3], [2, 4], [2, 4], [2, 4], [2, 4], [2, 3],
    [2, 2], [2, 4], [2, 2], [2, 4], [2, 4], [2, 4], [2, 2]  ])
    paises = np.array([ 13, 25, 18, 14, 6, 24, 2, 24, 24, 2, 19, 9, 18, 19, 26, 6, 4, 24, 4, 1, 12, 6, 3, 24, 23, 24, 2, 25, 11, 19, 25, 24, 7, 22, 2, 13, 16, 6, 6, 25, 15, 8, 2, 25, 21, 6, 13, 24, 14, 6, 5, 0, 13, 19, 7, 20, 24, 17, 27, 10, 19, 13, 25, 18, 14, 6, 24, 2, 24, 24, 2, 19, 9,
18, 19, 26, 6, 4, 24, 4, 1, 12, 6, 3, 24,
23, 24, 2, 25, 11, 19, 25, 24, 7, 22, 2, 13,
16, 6, 6, 25, 15, 8, 2, 25, 21, 6, 24,
14, 6, 5, 0, 13, 19, 7, 20, 24, 17, 27, 10, 
19, 13, 25, 18, 14, 6, 24, 2, 24, 24, 2, 19, 9,
18, 19, 26, 6, 4, 24, 4, 1, 12, 6, 3, 24,
23, 24, 2, 25, 19, 25, 24, 7, 22, 13,
16, 6, 6, 25, 15, 2, 25, 21, 6, 24,
14, 6, 5, 0, 13, 19, 7, 20, 24, 17, 27, 10,
19])
    paises = to_categorical(paises, num_classes=138)
    print(paises.shape[1])

    # Construir el modelo
    seo_input2 = Input(shape=(ligas.shape[1],), name='seo_input')
    dense_12 = Dense(64, activation='relu')(seo_input2)
    dense_22 = Dense(64, activation='relu')(dense_12)
    output2 = Dense(138, activation='softmax')(dense_22)

    model2 = Model(inputs=seo_input2, outputs=output2)
    model2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Entrenar el modelo
    model2.fit(ligas, paises, epochs=6000, batch_size=2)

    new_metrics2 = np.array([[liga,ligaDestino-1]])  # Asegurar que sea 2D
    pred2 = model2.predict(new_metrics2)
    max_valor=np.argmax(pred2)
    ligallegada=total[max_valor]
    print(ligallegada)
   

    
