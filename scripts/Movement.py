#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

# Se identifica ante ROS
rospy.init_node('joint_states_subscriber', anonymous=True)

# Se crea la función para recibir el mensaje del tópico
def callback(data):
    # Obtiene los nombres de las articulaciones
    joint_names = data.name
    # Obtiene los valores de las articulaciones
    joint_positions = data.position
    # Imprime los nombres y posiciones de las articulaciones
    for joint, position in zip(joint_names, joint_positions):
        print("Articulación:", joint, "| Posición:", position)

# Se suscribe al tópico "joint_states"
sub = rospy.Subscriber("joint_states", JointState, callback)

# Lo siguiente solo es para que el código no se cierre
rate = rospy.Rate(1)  # Frecuencia de 1Hz

# Bucle para mantener el nodo en ejecución
while not rospy.is_shutdown():
    rate.sleep()  # Delay de 1 segundo