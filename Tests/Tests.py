from math import sqrt

from scipy.stats import norm

from Generators.Lehmer import Lehmer


def check_equality_of_signs(bit_seq, alpha):
    bytes = {}
    m = len(bit_seq) / 8
    n_j = m // 256

    for i in range(0, int(8 * len(bit_seq)), 8):
        byte = bit_seq[i:i + 8]
        if byte in bytes:
            bytes[byte] += 1
        else:
            bytes[byte] = 1

    xi_2 = 0
    for key, value in bytes.items():
        xi_2 += pow(value - n_j, 2) / n_j

    z_alpha = norm.ppf(1 - alpha)
    xi_2_alpha = sqrt(2 * 255) * z_alpha + 255

    return xi_2 <= xi_2_alpha


def check_independence_of_signs(bit_seq, alpha):
    bytes = []
    bytes_pair = {}
    bytes_i = {}
    bytes_j = {}
    for i in range(0, int(8 * len(bit_seq)), 8):
        byte = bit_seq[i:i + 8]
        bytes.append(byte)
    for i in range(0, len(bytes) - 1):
        if (bytes[i], bytes[i + 1]) in bytes_pair:
            bytes_pair[bytes[i], bytes[i + 1]] += 1
        else:
            bytes_pair[bytes[i], bytes[i + 1]] = 1
        if bytes[i] in bytes_i:
            bytes_i[bytes[i]] += 1
        else:
            bytes_i[bytes[i]] = 1
        if bytes[i + 1] in bytes_j:
            bytes_j[bytes[i + 1]] += 1
        else:
            bytes_j[bytes[i + 1]] = 1

    xi_2 = 0
    m = len(bytes)
    n = m // 2
    for i in bytes:
        for j in bytes:
            if bytes_i[i] != 0 and bytes_j[i] != 0 and (i, j) in bytes_pair:
                xi_2 += pow(bytes_pair[(i, j)], 2) / (bytes_i[i] * bytes_j[i])

    xi_2 = n * (xi_2 - 1)
    z_alpha = norm.ppf(1 - alpha)
    xi_2_alpha = sqrt(2 * pow(255, 2)) * z_alpha + pow(255, 2)

    return xi_2 <= xi_2_alpha


def check_homogeneity_of_bin_seq(bit_seq, alpha):
    bytes = []
    r = 32
    for i in range(0, len(bit_seq), 8):
        bytes.append(bit_seq[i:i + 8])
    m_ = len(bytes) // r
    n = m_ * r
    print("Hey")
    bytes_r = [bytes[i * m_:(i + 1) * m_] for i in range(r)]
    xi_2 = 0
    for i in bytes:
        print(f"Hui {xi_2}")
        v_i = sum(sublist.count(i) for sublist in bytes_r)
        for j in bytes_r:
            xi_2 += pow(j.count(i), 2) / (m_ * v_i)
    xi_2 = n * (xi_2 - 1)
    z_alpha = norm.ppf(1 - alpha)
    print(z_alpha)
    xi_2_alpha = sqrt(2 * 255*(r-1)) * z_alpha + 255*(r-1)
    print(xi_2_alpha)
    return xi_2 <= xi_2_alpha


lehmer = Lehmer()
bit_sequence = lehmer.generate_lehmer_high(1000000)
print(bit_sequence)
print(check_homogeneity_of_bin_seq(bit_sequence, 0.1))
