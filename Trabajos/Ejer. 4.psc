Algoritmo Ejercicio_4
	// �rea de documentaci�n
	// Enunciado: determinar el tiempo (en segundos) que le toma a un veh�culo para llegar a una velocidad espec�fica
	// Versi�n: 1.0
	// Desarrollado por: Jeronimo Sepulveda
	// Fecha: 26/02/23
	
	// �rea de definici�n de variables
	Definir v_Ini Como Real; // variable de entrada que almacena la velocidad inicial (en m/seg)
	Definir v_FinKilHor Como Real; // variable de entrada que almacena la velocidad final (en kil/hr)
	Definir v_ac Como Real; // variable de entrada que almacena la aceleraci�n (en m/seg^2)
	Definir c_facCon Como Real; // constante que almacena el factor de conversi�n de kil/hr a m/seg
	Definir v_FinMetSeg Como Real; // variable de salida que almacena la velocidad final (en m/seg)
	Definir v_tf Como Real; // variable de salida que almacena el tiempo (en seg)
	
	// Inicializaci�n de variables
	v_Ini = 0.0;
	v_FinKilHor = 0.0;
	v_ac = 0.0;
	c_facCon = 0.278;
	v_FinMetSeg = 0.0;
	v_tf = 0.0;
	
	// �rea de entradas
	Escribir "Digite la velocidad inicial en m/seg: "
	Leer v_Ini;
	
	Escribir "Digite la aceleraci�n en m/seg^2: ";
	Leer v_ac;
	
	Escribir "Digite la velocidad final en kil/hr: ";
	Leer v_FinKilHor;
	
	// �rea de procesos
	v_FinMetSeg = v_FinKilHor * c_facCon
	v_tf = (v_FinMetSeg - v_Ini) / v_ac
	
	// �rea de salidas
	Escribir "La velocidad en m/seg es de: ", v_FinMetSeg
	
	Escribir "El tiempo en segundos es de: ", v_tf
	
FinAlgoritmo
