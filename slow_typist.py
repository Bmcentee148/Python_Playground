from math import sqrt
key_positions = {
'1' : (0,0), '2' : (0,1), '3' : (0,2), 
'4' : (1,0), '5' : (1,1), '6' : (1,2),
'7' : (2,0), '8' : (2,1), '9' : (2,2),
'.' : (3,0), '0' : (3,1)
}

def key_dist(key1, key2) :
    """ Computes the distance between two given keys given their position 
        obtained from the key position dictionary. """
    return sqrt((key_positions[key1][0] - key_positions[key2][0])**2 + 
        (key_positions[key1][1] - key_positions[key2][1])**2 )

def get_distance(key_sequence) :
    total_distance = 0
    for i in range(len(key_sequence) - 1) :
        total_distance += key_dist(key_sequence[i], key_sequence[i+1])
    return total_distance

def get_ips() :
    print "Enter each ip line by line:"
    ips = []
    ip = raw_input('> ')
    while ip :
        ips.append(ip.strip(" "))
        ip = raw_input('> ')
    print ips
    return ips

def main() :
    ips_to_type = get_ips()
    for ip in ips_to_type :
        print ip, "=>", round(get_distance(ip), 2), "\bcm"

if __name__ == "__main__" :
    main()
