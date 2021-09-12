N = int(input("ВВедите N:"))

# вычисляем длину последней строки
n = N
fn = 1

for i in range(2, n):
    fn *= i

last_row_count = 0
for k in range(0, n):
    count = 0
    fk = 1
    for i_k in range(2, k + 1):
        fk *= i_k

    fnk = 1
    for i_nk in range(2, n - k):
        fnk *= i_nk

    Cnk = fn // (fk * fnk)

    while Cnk != 0:
        Cnk //= 10
        count += 1
    last_row_count += count

# print(f"last row count: {last_row_count + n - 1}")

for i in range(N):

    # вычисляем длину текущей строки
    cur_row_count = 0
    fn = 1
    for i_n in range(2, i+1):
        fn *= i_n

    for k in range(0, i+1):
        count = 0

        fk = 1
        for i_k in range(2, k + 1):
            fk *= i_k

        fnk = 1
        for i_nk in range(2, i - k + 1):
            fnk *= i_nk

        Cnk = fn // (fk * fnk)

        while Cnk != 0:
            Cnk //= 10
            count += 1
        cur_row_count += count
    # print(f"длина текущей строки {i}: {cur_row_count + i}")

    # # вычисляем длину следующей строки
    # i_next = i + 1
    # next_row_count = 0
    # fn = 1
    # for i_n in range(2, i_next+1):
    #     fn *= i_n
    #
    # for k in range(0, i_next+1):
    #     count = 0
    #
    #     fk = 1
    #     for i_k in range(2, k + 1):
    #         fk *= i_k
    #
    #     fnk = 1
    #     for i_nk in range(2, i_next - k + 1):
    #         fnk *= i_nk
    #
    #     Cnk = fn // (fk * fnk)
    #
    #     while Cnk != 0:
    #         Cnk //= 10
    #         count += 1
    #     next_row_count += count
    # print(f"длина следующей строки {i}: {next_row_count + i_next}")

    # ------------------------------
    # выводим пробелы
    count_spaces = (last_row_count + n - 1) - (cur_row_count + i)
    # print(f"count spaces: {count_spaces}")
    for l in range(count_spaces//2):
        print(" ", end ="")

    for k in range(0, i + 1):
        fi = 1
        for i_n in range(2, i + 1):
            fi *= i_n

        fk = 1
        for j in range(2, k + 1):
            fk *= j

        fik = 1
        for i_k in range(2, i - k + 1):
            fik *= i_k

        Cik = fi // (fk * fik)

        print(Cik, end=' ')
    print()
