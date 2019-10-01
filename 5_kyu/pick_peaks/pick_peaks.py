def pick_peaks(arr):
    pos = []
    peaks = []
    m_p = 1
    while m_p < len(arr)-1:
        if arr[m_p] > arr[m_p - 1]:
            if arr[m_p] > arr[m_p + 1]:
                pos.append(m_p)
                peaks.append(arr[m_p])
            elif arr[m_p] == arr[m_p+1]:
                temp = m_p
                for i in range(temp+1, len(arr)):
                    if arr[i] < arr[temp]:
                        pos.append(temp)
                        peaks.append(arr[temp])
                        m_p = i
                        break
                    elif arr[i] > arr[temp]:
                        m_p = i-1
                        break
        m_p += 1
    return {'pos': pos, 'peaks': peaks}
