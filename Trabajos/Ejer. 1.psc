Algoritmo Ejercicio_1
	// �rea de documentaci�n
	// Enunciado: determinar la aceleraci�n (en m/seg^2) de un veh�culo seg�n su velocidad (en m/seg) y su tiempo (en segundos)
	// Versi�n: 1.0
	// Desarrollado por: Jeronimo Sepulveda
	// Fecha: 26/02/23
	
	// �rea de definici�n de variables
	Definir v_Ini Como Real; // variable de entrada que almacena la velocidad inicial (en m/seg)
	Definir v_Fin Como Real; // variable de entrada que almacena la velocidad final (en m/seg)
	Definir v_tf Como Real; // variable de entrada que almacena el tiempo (en seg)
	Definir v_ac Como Real; // variable de salida que almacena la aceleraci�n (en m/seg^2)
	
	// Inicializaci�n de variables
	v_Ini = 20;
	v_Fin = 25;
	v_tf = 5;
	v_ac = 0.0;
	
	// �rea de entradas
	Escribir "Digite la velocidad inicial en m/seg: "
	Leer v_Ini
	
	Escribir "Digite la velocidad final en m/seg: "
	Leer v_Fin
	
	Escribir "Digite el tiempo en segundos: "
	Leer v_tf
	
	// �rea de procesos
	v_ac = (v_Fin - v_Ini) / v_tf
	
	// �rea de salidas
	Escribir "La aceleraci�n en m/seg^2 es de: ", v_ac
	
FinAlgoritmo
