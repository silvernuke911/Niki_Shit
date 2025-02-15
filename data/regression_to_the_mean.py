import numpy as np
import matplotlib.pyplot as plt

N = 100
test_answers = np.random.choice([0,1], N)
print(test_answers)
N_students = 1000000
test_freq = np.zeros(N+1, dtype=int)

for i in range(N_students):
    #print(i, end='\r')
    score = 0
    student_answer = np.random.choice([0,1], N)
    for j in range(N):
        if student_answer[j] == test_answers[j]:
            score += 1
    test_freq[score] += 1
print(test_freq)

def normal_pdf(x, mu, sigma):
    """Computes the PDF of a normal distribution at x."""
    coeff = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    return coeff * exponent

x = np.arange(0,100,0.1)
normal_pdfg = normal_pdf(x, 50, np.sqrt(N*(0.5*0.5))) * N_students
plt.plot(x, normal_pdfg, color = 'r', linewidth=2)
plt.xlim(0,100)
plt.xticks(range(0,105,5))
plt.bar(range(N+1), test_freq, width = 1, edgecolor = 'k')
plt.grid(True, linestyle = '--', alpha = 0.7)
plt.show()