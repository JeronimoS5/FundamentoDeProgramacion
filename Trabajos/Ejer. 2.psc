Algoritmo Ejercicio_2
	// �rea de documentaci�n
	// Enunciado: determinar la aceleraci�n (en m/seg^2) de un veh�culo seg�n su velocidad (en kil/hr) y su tiempo (en segundos)
	// Versi�n: 1.0
	// Desarrollado por: Jeronimo Sepulveda
	// Fecha: 26/02/23
	
	// �rea de definici�n de variables
	Definir v_Ini Como Entero; // variable de entrada que almacena la velocidad inicial (en m/seg)
	Definir v_FinKilHor Como Entero; // variable de entrada que almacena la velocidad final (en kil/hr)
	Definir v_tf Como Entero; // variable de entrada que almacena el tiempo (en segundos)
	Definir v_FinMetSeg Como Real; // variable de salida que almacena la velocidad final (en m/seg)
	Definir c_facCon Como Real; // constante que almacena el factor de conversi�n de kil/hr a m/seg
	Definir v_ac Como Real; // variable de salida que almacena la aceleraci�n (en m/seg^2)
	
	// Inicializaci�n de variables
	v_Ini = 0;
	v_FinKilHor = 0;
	v_tf = 0;
	v_FinMetSeg = 0.0;
	c_facCon = 0.278;
	v_ac = 0.0;
	
	// �rea de entradas
	Escribir "Digite la velocidad inicial en m/seg: ";
	Leer v_Ini;
	
	Escribir "Digite la velocidad final en kil/hora: ";
	Leer v_FinKilHor;
	
	Escribir "Digite el tiempo en segundos: "
	Leer v_tf;
	
	// �rea de procesos
	v_FinMetSeg = v_FinKilHor * c_facCon
	v_ac = (v_FinMetSeg - v_Ini) / v_tf
	
	// �rea de salidas
	Escribir "La velocidad final en met/seg es de: ", v_FinMetSeg
	
	Escribir "La aceleraci�n en m/seg^2 es de: ", v_ac
	
FinAlgoritmo
