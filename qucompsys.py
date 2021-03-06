# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 01:43:16 2021

@author: AndreaB.Rava
"""
import numpy as np
import qutip as qu

def n_rand_qubits(n_qubits):
    """
    This method generates a list of random n qubits

    Parameters
    ----------
    n_qubits : int
        number of qubits.

    Raises
    ------
    ValueError
        if number of qubits is less than 1.

    Returns
    -------
    list_n_rand_qubits : list
        a list of n qubits.

    """
    if n_qubits < 1:
        raise ValueError('number of qubits must be > 0, but is {}'.format(n_qubits))
    list_n_rand_qubits = []
    i = 0
    coeffs_real = np.random.random_sample((2,n_qubits))
    coeffs_imm = np.random.random_sample((2,n_qubits))
    basis_elem = np.random.randint(0,2,(2,n_qubits))
    for i in range(n_qubits):
        gen_qubit = (complex(coeffs_real[0][i],coeffs_imm[0][i])*qu.basis(2,basis_elem[0][i])
                     + complex(coeffs_real[1][i],coeffs_imm[1][i])*qu.basis(2,basis_elem[1][i])).unit()
        list_n_rand_qubits.append(gen_qubit)
    return list_n_rand_qubits


def n_qeye(n_qubits):
    """
    This method generates a tensor that apply identity on a state
    of n-qubits

    Parameters
    ----------
    n_qubits : int
        number of qubits the state is composed of.

    Raises
    ------
    ValueError
        if number of qubits is less than 1.

    Returns
    -------
    tensor (Qobj)
        a tensor that apply the identity to a n-qubits state.

    """
    if n_qubits < 1:
        raise ValueError('number of qubits must be > 0, but is {}'.format(n_qubits))
    return qu.tensor([qu.qeye(2)]*n_qubits)


def n_sigmax(n_qubits, qubit_pos):
    """
    This method generates a tensor(Qobj) wich perform a single-qubit sigmax operation
    on a state of n-qubits

    Parameters
    ----------
    n_qubits : int
        number of qubits the states is composed of.
    qubit_pos : int
        qubit on which the sigmax operator acts (position starts at '0').

    Raises
    ------
    ValueError
        if number of qubits is less than 2
    ValueError
        if qubit position is < 0 or > n_qubits-1

    Returns
    -------
    n_sigmax: tensor (Qobj)
        a tensor that apply sigmax on the nth-qubit of a n-qubits state.

    """
    if n_qubits < 1:
        raise ValueError('number of vertices must be > 0, but is {}'.format(n_qubits))
    if qubit_pos < 0 or qubit_pos > n_qubits-1:
        raise ValueError('qubit position must be > 0 or < n_qubits-1, but is {}'.format(qubit_pos))
    list_n_sigmax = []
    for i in range(n_qubits):
        list_n_sigmax.append(qu.tensor([qu.qeye(2)]*i+[qu.sigmax()]+[qu.qeye(2)]*(n_qubits-i-1)))
    return list_n_sigmax[qubit_pos]


def n_sigmay(n_qubits, qubit_pos):
    """
    This method generates a tensor(Qobj) wich perform a single-qubit sigmay operation
    on a state of n-qubits

    Parameters
    ----------
    n_qubits : int
        number of qubits the states is composed of.
    qubit_pos : int
        qubit on which the sigmax operator acts (position starts at '0').

    Raises
    ------
    ValueError
        if number of qubits is less than 2
    ValueError
        if qubit position is < 0 or > n_qubits-1

    Returns
    -------
    n_sigmaz: tensor (Qobj)
        a tensor that apply sigmay on the nth-qubit of a n-qubits state.

    """
    if n_qubits < 1:
        raise ValueError('number of vertices must be > 0, but is {}'.format(n_qubits))
    if qubit_pos < 0 or qubit_pos > n_qubits-1:
        raise ValueError('qubit position must be > 0 or < n_qubits-1, but is {}'.format(qubit_pos))
    list_n_sigmay = []
    for i in range(n_qubits):
        list_n_sigmay.append(qu.tensor([qu.qeye(2)]*i+[qu.sigmay()]+[qu.qeye(2)]*(n_qubits-i-1)))
    return list_n_sigmay[qubit_pos]


def n_sigmaz(n_qubits, qubit_pos):
    """
    This method generates a tensor(Qobj) wich perform a single-qubit sigmaz operation
    on a state of n-qubits

    Parameters
    ----------
    n_qubits : int
        number of qubits the states is composed of.
    qubit_pos : int
        qubit on which the sigmax operator acts (position starts at '0').

    Raises
    ------
    ValueError
        if number of qubits is less than 2
    ValueError
        if qubit position is < 0 or > n_qubits-1

    Returns
    -------
    n_sigmaz: tensor (Qobj)
        a tensor that apply sigmaz on the nth-qubit of a n-qubits state.

    """
    if n_qubits < 1:
        raise ValueError('number of vertices must be > 0, but is {}'.format(n_qubits))
    if qubit_pos < 0 or qubit_pos > n_qubits-1:
        raise ValueError('qubit position must be > 0 or < n_qubits-1, but is {}'.format(qubit_pos))
    list_n_sigmaz = []
    for i in range(n_qubits):
        list_n_sigmaz.append(qu.tensor([qu.qeye(2)]*i+[qu.sigmaz()]+[qu.qeye(2)]*(n_qubits-i-1)))
    return list_n_sigmaz[qubit_pos]

def comp_basis_prob_dist(qstate):
    """
    This methos gives the probability distribution of a given state in the computational
    basis state

    Parameters
    ----------
    qstate : a qobject, 1-D array-like
        a tendor representing a n-qubits state.

    Returns
    -------
    prob_dist : list
        list of the probabilities distribution.

    """
    prob_dist = []
    for component in qstate.full():
        prob_dist.append(float(abs(component))**2)
    return prob_dist
