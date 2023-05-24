Algoritmo Ejemplo_Pag73
	// �rea de documentaci�n
	// Enunciado: calcular el salario bruto y el salario neto de un trabajador "por horas" conociendo el nombre, n�mero de horas trabajadas, impuestos a pagar y salario neto
	// Versi�n: 1.0
	// Desarrollado por: Jeronimo Sepulveda
	// Fecha: 03/03/23
	
	// �rea de definici�n de variables
	Definir v_nom Como Caracter; //variable que almacena el nombre del trabajador
	Definir v_hor Como Entero; //variable que almacena las horas trabajadas
	Definir v_preHor Como Real; //variable que almacena el precio por hora
	Definir v_salBru Como Real; //variable que almacena el salario bruto
	Definir v_tas Como Real; //variable que almacena las tasas de intereses
	Definir v_salNet Como Real; //variable que almacena el salario neto
	
	// Inicializaci�n de variables
	v_nom = " "
	v_hor = 0;
	v_preHor = 0.0;
	v_salBru = 0.0;
	v_tas = 0.0;
	v_salNet = 0.0;
	
	// �rea de entradas
	Escribir "Digite el nombre del trabajador: ";
	Leer v_nom;
	
	Escribir "Digite las horas trabajadas: ";
	Leer v_hor;
	
	Escribir "Digite el precio por hora trabajada: ";
	Leer v_preHor;
	
	// �rea de procesos
	v_salBru = v_hor * v_preHor
	v_tas = 0.25 * v_salBru
	v_salNet = (v_salBru - v_tas)
	
	// �rea de salidas
	Escribir "El trabajador ", v_nom " recibe un salario bruto igual a: ", v_salBru " y un salario neto igual a: ", v_salNet
FinAlgoritmo
