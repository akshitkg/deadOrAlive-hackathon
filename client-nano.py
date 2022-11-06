from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from numpy.random import randint
import numpy as np
import os

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import random_statevector, Statevector
from qiskit.visualization import plot_bloch_multivector, array_to_latex,plot_histogram
from qiskit.extensions import Initialize
from qiskit import Aer,transpile,assemble
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
# import os
from qiskit.ignis.verification import marginal_counts


def key_to_bytes(key):
    stringConcat=''
    for elem in key:
        stringConcat+=(str(elem))
    return stringConcat





def generate_key():



    qc = QuantumCircuit(1,1)
    # Alice prepares qubit in state |+>
    qc.h(0)
    qc.barrier()
    # Alice now sends the qubit to Bob
    # who measures it in the X-basis
    qc.h(0)
    qc.measure(0,0)

    # Draw and simulate circuit
    # display(qc.draw())
    aer_sim = Aer.get_backend('aer_simulator')
    job = aer_sim.run(assemble(qc))
    # plot_histogram(job.result().get_counts())



    qc = QuantumCircuit(1,1)
    # Alice prepares qubit in state |+>
    qc.h(0)
    # Alice now sends the qubit to Bob
    # but Eve intercepts and tries to read it
    qc.measure(0, 0)
    qc.barrier()
    # Eve then passes this on to Bob
    # who measures it in the X-basis
    qc.h(0)
    qc.measure(0,0)


    np.random.seed(seed=0)
    n = 100
    ## Step 1
    # Alice generates bits
    alice_bits = randint(2, size=n)
    print(alice_bits)


    np.random.seed(seed=0)
    n = 100
    ## Step 1
    #Alice generates bits
    alice_bits = randint(2, size=n)

    ## Step 2
    # Create an array to tell us which qubits
    # are encoded in which bases
    alice_bases = randint(2, size=n)
    print(alice_bases)


    def encode_message(bits, bases):
        message = []
        for i in range(n):
            qc = QuantumCircuit(1,1)
            if bases[i] == 0: # Prepare qubit in Z-basis
                if bits[i] == 0:
                    pass 
                else:
                    qc.x(0)
            else: # Prepare qubit in X-basis
                if bits[i] == 0:
                    qc.h(0)
                else:
                    qc.x(0)
                    qc.h(0)
            qc.barrier()
            message.append(qc)
        return message


    np.random.seed(seed=0)
    n = 100

    ## Step 1
    # Alice generates bits
    alice_bits = randint(2, size=n)

    ## Step 2
    # Create an array to tell us which qubits
    # are encoded in which bases
    alice_bases = randint(2, size=n)
    message = encode_message(alice_bits, alice_bases)



    print('bit = %i' % alice_bits[0])
    print('basis = %i' % alice_bases[0])



    print('bit = %i' % alice_bits[4])
    print('basis = %i' % alice_bases[4])
    message[4].draw()




    np.random.seed(seed=0)
    n = 100

    ## Step 1
    # Alice generates bits
    alice_bits = randint(2, size=n)

    ## Step 2
    # Create an array to tell us which qubits
    # are encoded in which bases
    alice_bases = randint(2, size=n)
    message = encode_message(alice_bits, alice_bases)

    ## Step 3
    # Decide which basis to measure in:
    bob_bases = randint(2, size=n)
    print(bob_bases)


    def measure_message(message, bases):
        backend = Aer.get_backend('aer_simulator')
        measurements = []
        for q in range(n):
            if bases[q] == 0: # measuring in Z-basis
                message[q].measure(0,0)
            if bases[q] == 1: # measuring in X-basis
                message[q].h(0)
                message[q].measure(0,0)
            aer_sim = Aer.get_backend('aer_simulator')
            qobj = assemble(message[q], shots=1, memory=True)
            result = aer_sim.run(qobj).result()
            measured_bit = int(result.get_memory()[0])
            measurements.append(measured_bit)
        return measurements


    np.random.seed(seed=0)
    n = 100

    ## Step 1
    # Alice generates bits
    alice_bits = randint(2, size=n)

    ## Step 2
    # Create an array to tell us which qubits
    # are encoded in which bases
    alice_bases = randint(2, size=n)
    message = encode_message(alice_bits, alice_bases)

    ## Step 3
    # Decide which basis to measure in:
    bob_bases = randint(2, size=n)
    bob_results = measure_message(message, bob_bases)



    # message[0].draw()


    # message[6].draw()


    print(bob_results)


    def remove_garbage(a_bases, b_bases, bits):
        good_bits = []
        for q in range(n):
            if a_bases[q] == b_bases[q]:
                # If both used the same basis, add
                # this to the list of 'good' bits
                good_bits.append(bits[q])
        return good_bits


    np.random.seed(seed=0)
    n = 100

    ## Step 1
    # Alice generates bits
    alice_bits = randint(2, size=n)

    ## Step 2
    # Create an array to tell us which qubits
    # are encoded in which bases
    alice_bases = randint(2, size=n)
    message = encode_message(alice_bits, alice_bases)

    ## Step 3
    # Decide which basis to measure in:
    bob_bases = randint(2, size=n)
    bob_results = measure_message(message, bob_bases)

    ## Step 4
    alice_key = remove_garbage(alice_bases, bob_bases, alice_bits)
    print(alice_key)



    np.random.seed(seed=0)
    n = 100

    ## Step 1
    # Alice generates bits
    alice_bits = randint(2, size=n)

    ## Step 2
    # Create an array to tell us which qubits
    # are encoded in which bases
    alice_bases = randint(2, size=n)
    message = encode_message(alice_bits, alice_bases)

    ## Step 3
    # Decide which basis to measure in:
    bob_bases = randint(2, size=n)
    bob_results = measure_message(message, bob_bases)

    ## Step 4
    alice_key = remove_garbage(alice_bases, bob_bases, alice_bits)
    bob_key = remove_garbage(alice_bases, bob_bases, bob_results)
    print(alice_key)
    print(bob_key)


    def sample_bits(bits, selection):
        sample = []
        for i in selection:
            # use np.mod to make sure the
            # bit we sample is always in 
            # the list range
            i = np.mod(i, len(bits))
            # pop(i) removes the element of the
            # list at index 'i'
            sample.append(bits.pop(i))
        return sample



    np.random.seed(seed=0)
    n = 100

    ## Step 1
    # Alice generates bits
    alice_bits = randint(2, size=n)

    ## Step 2
    # Create an array to tell us which qubits
    # are encoded in which bases
    alice_bases = randint(2, size=n)
    message = encode_message(alice_bits, alice_bases)

    ## Step 3
    # Decide which basis to measure in:
    bob_bases = randint(2, size=n)
    bob_results = measure_message(message, bob_bases)

    ## Step 4
    alice_key = remove_garbage(alice_bases, bob_bases, alice_bits)
    bob_key = remove_garbage(alice_bases, bob_bases, bob_results)

    ## Step 5
    sample_size = 15
    bit_selection = randint(n, size=sample_size)

    bob_sample = sample_bits(bob_key, bit_selection)
    print("  bob_sample = " + str(bob_sample))
    alice_sample = sample_bits(alice_key, bit_selection)
    print("alice_sample = "+ str(alice_sample))



    bob_sample==alice_sample

    print("Private key Alice has: ", alice_key)
    print("Private key Bob has: ",bob_key)

    return alice_key



def create_crypter(password):
    # print(type(password))
    passByte=bytes(password, 'utf-8')
  
    salt=os.urandom(16)
    kdf=PBKDF2HMAC(algorithm=hashes.SHA256,length=32,salt=salt,iterations=10,backend=default_backend())
    key=base64.urlsafe_b64encode(kdf.derive(passByte))
    crypter=Fernet(key)
    return crypter



# import socket
# ClientMultiSocket = socket.socket()
# host = '127.0.0.1'
# port = 2007
# print('Waiting for connection response')
# try:
#     ClientMultiSocket.connect((host, port))
# except socket.error as e:
#     print(str(e))
# res = ClientMultiSocket.recv(1024)
# while True:
#     Input = input('Hey there: ')
#     ClientMultiSocket.send(str.encode(Input))
#     res = ClientMultiSocket.recv(1024)
#     print(res.decode())
# ClientMultiSocket.close()


key=generate_key()
keyByte=key_to_bytes(key)
crypter=create_crypter(keyByte)
enc=crypter.encrypt(b"Hello World")
print("encrypted",enc)
print()
decrypted=crypter.decrypt(enc)
print("decrypted",decrypted)