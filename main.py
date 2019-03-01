


class Image:

    def __init__(self, filename):
        with open(filename, 'r') as f:
            img = f.read()
            rows = img.split('\n')
            rows.pop()
            self.pixels = []
            self.type = rows.pop(0)
            self.width = int(rows[0].split(' ')[0])
            self.height = int(rows[0].split(' ')[1])
            rows.pop(0)
            self.smth = rows[0]
            rows.pop(0)
            self.get_pixels(rows)


    def get_pixels(self, rows):
        self.pixels = []
        if self.type=='P2':
            for i in rows:
                current_row = i.split(' ')
                if current_row[len(current_row)-1] == '':
                    current_row.pop()
                self.pixels.append([int(element) for element in current_row])


    def save_image(self, filename):
        with open (filename, 'w') as f:
            if self.type == 'P2':
                f.write('P2\n')
                f.write(str(self.width) + ' ' + str(self.height) + "\n")
                f.write(str(255) + "\n")
                for i in self.pixels:
                    for j in i:
                        f.write(str(j) + " ")
                    f.write("\n")


class Compressor:

    def __init__(self):
        pass

    def rleP2(self, pixels):
        res = []
        for i in pixels:
            prev = ''
            row = []
            count = 1
            for j in i:
                if prev == '':
                    prev = j
                elif prev == j:
                    count += 1
                else:
                    row.append((prev, count))
                    prev = j
                    count = 1
            res.append(row)
        return res