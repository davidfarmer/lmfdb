
import sage

graph_type={}

graphG="""
<svg viewBox="0 0 1600 750" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
  <path d="M 200 125 L 800 125 " stroke="_edgecolor_" stroke-width="9" />
  <text x="500.0" y="95.0" text-anchor="middle" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >3</text>
  <path d="M 200 125 L 200 625 " stroke="_edgecolor_" stroke-width="9" />
  <text x="230.0" y="375.0" text-anchor="start" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >2</text>
  <path d="M 800 125 L 1400 125 " stroke="_edgecolor_" stroke-width="9" />
  <text x="1100.0" y="95.0" text-anchor="middle" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >3</text>
  <path d="M 800 125 L 800 625 " stroke="_edgecolor_" stroke-width="9" />
  <text x="830.0" y="375.0" text-anchor="start" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >2</text>
  <path d="M 1400 125 L 1400 625 " stroke="_edgecolor_" stroke-width="9" />
  <text x="1430.0" y="375.0" text-anchor="start" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >2</text>
  <path d="M 200 625 L 800 625 " stroke="_edgecolor_" stroke-width="9" />
  <text x="500.0" y="595.0" text-anchor="middle" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >3</text>
  <path d="M 800 625 L 1400 625 " stroke="_edgecolor_" stroke-width="9" />
  <text x="1100.0" y="595.0" text-anchor="middle" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >3</text>
  <path d="M 50 50 L 50 200 L 350 200 L 350 50 L 50 50 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="200" y="135" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="/EllipticCurve/Q/112/c/1">_curve2label_</a></text>
  <text x="59.0" y="188.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >1.4</text>
  <text x="341.0" y="188.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >[2]</text>
  <text x="341.0" y="80.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >144</text>
  <path d="M 650 50 L 650 200 L 950 200 L 950 50 L 650 50 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="800" y="135" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="/EllipticCurve/Q/112/c/3">_curve0label_</a></text>
  <text x="659.0" y="188.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >1.4</text>
  <text x="941.0" y="188.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >[2]</text>
  <text x="941.0" y="80.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >48</text>
  <path d="M 1250 50 L 1250 200 L 1550 200 L 1550 50 L 1250 50 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="1400" y="135" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="/EllipticCurve/Q/112/c/4">_curve4label_</a></text>
  <text x="1259.0" y="188.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >1.4</text>
  <text x="1541.0" y="188.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >[2]</text>
  <text x="1541.0" y="80.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >16</text>
  <path d="M 50 550 L 50 700 L 350 700 L 350 550 L 50 550 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="200" y="635" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="/EllipticCurve/Q/112/c/6">_curve3label_</a></text>
  <text x="59.0" y="688.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >1.4</text>
  <text x="341.0" y="688.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >[2]</text>
  <text x="341.0" y="580.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >24</text>
  <path d="M 650 550 L 650 700 L 950 700 L 950 550 L 650 550 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="800" y="635" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="/EllipticCurve/Q/112/c/2">_curve1label_</a></text>
  <text x="659.0" y="688.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >1.4</text>
  <text x="941.0" y="688.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >[2]</text>
  <text x="941.0" y="580.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >72</text>
  <path d="M 1250 550 L 1250 700 L 1550 700 L 1550 550 L 1250 550 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="1400" y="635" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="/EllipticCurve/Q/112/c/5">_curve5label_</a></text>
  <text x="1259.0" y="688.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >1.4</text>
  <text x="1541.0" y="688.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >[2]</text>
  <text x="1541.0" y="580.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >8</text>
  <text x="1541.0" y="730.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >optimal</text>
 /svg>
"""

graphH = """
<svg viewBox="0 0 1600 950" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">

  <path d="M 200 125 L 500 475 " stroke="_edgecolor_" stroke-width="9" />
  <text x="371.0" y="290.0" text-anchor="start" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >2</text>
  <path d="M 500 475 L 1100 475 " stroke="_edgecolor_" stroke-width="9" />
  <text x="800.0" y="445.0" text-anchor="middle" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >2</text>
  <path d="M 1100 475 L 1400 125 " stroke="_edgecolor_" stroke-width="9" />
  <text x="1229.0" y="290.0" text-anchor="end" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >2</text>
  <path d="M 200 825 L 500 475 " stroke="_edgecolor_" stroke-width="9" />
  <text x="329.0" y="650.0" text-anchor="end" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >2</text>
  <path d="M 1100 475 L 1400 825 " stroke="_edgecolor_" stroke-width="9" />
  <text x="1271.0" y="650.0" text-anchor="start" fill="_degreecolor_" style="font-family:verdana;font-size:250%" >2</text>
  
  <path d="M 50 50 L 50 200 L 350 200 L 350 50 L 50 50 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="200" y="135" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="_curve2urlcremona_">_curve2label_</a></text>
  <text x="59.0" y="188.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >_curve2sha_&middot;_curve2tamagawa_</text>
  <text x="341.0" y="188.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve2torsion_</text>
  <text x="341.0" y="80.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve2degree_</text>
  <text x="62" y="230.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >_optimal2_</text>
  <path d="M 1250 50 L 1250 200 L 1550 200 L 1550 50 L 1250 50 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="1400" y="135" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="_curve4urlcremona_">_curve4label_</a></text>
  <text x="1259.0" y="188.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >_curve4sha_&middot;_curve4tamagawa_</text>
  <text x="1541.0" y="188.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve4torsion_</text>
  <text x="1541.0" y="80.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve4degree_</text>
  <text x="1541.0" y="230.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_optimal4_</text>
  <path d="M 350 400 L 350 550 L 650 550 L 650 400 L 350 400 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="500" y="485" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="_curve0urlcremona_">_curve0label_</a></text>
  <text x="359.0" y="538.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >_curve0sha_&middot;_curve0tamagawa_</text>
  <text x="641.0" y="538.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve0torsion_</text>
  <text x="641.0" y="430.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve0degree_</text>
  <text x="641.0" y="580.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_optimal0_</text>
  <path d="M 950 400 L 950 550 L 1250 550 L 1250 400 L 950 400 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="1100" y="485" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="_curve1urlcremona_">_curve1label_</a></text>
  <text x="959.0" y="538.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >_curve1sha_&middot;_curve1tamagawa_</text>
  <text x="1241.0" y="538.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve1torsion_</text>
  <text x="1241.0" y="430.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve1degree_</text>
  <text x="961" y="580.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >_optimal1_</text>
  <path d="M 50 750 L 50 900 L 350 900 L 350 750 L 50 750 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="200" y="835" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="_curve3urlcremona_">_curve3label_</a></text>
  <text x="59.0" y="888.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >_curve3sha_&middot;_curve3tamagawa_</text>
  <text x="341.0" y="888.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve3torsion_</text>
  <text x="341.0" y="780.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve3degree_</text>
  <text x="61" y="930.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >_optimal3_</text>
  <path d="M 1250 750 L 1250 900 L 1550 900 L 1550 750 L 1250 750 " stroke="#900" fill="#fff" stroke-width="5" />
  <text x="1400" y="835" text-anchor="middle" fill="_labelcolor_" style="font-family:verdana;font-size:300%" ><a href="_curve5urlcremona_">_curve5label_</a></text>
  <text x="1259.0" y="888.0" text-anchor="start" fill="#000" style="font-family:verdana;font-size:200%" >_curve5sha_&middot;_curve5tamagawa_</text>
  <text x="1541.0" y="888.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve5torsion_</text>
  <text x="1541.0" y="780.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_curve5degree_</text>
  <text x="1541.0" y="930.0" text-anchor="end" fill="#000" style="font-family:verdana;font-size:200%" >_optimal5_</text>
  
</svg>
"""

graph_type['G'] = graphG
graph_type['H'] = graphH

def graph_svg(isogeny_class):

    isogeny_matrix = isogeny_class.isogeny_matrix
#    the_conductor = isogeny_class.conductor

    print "the curves are", isogeny_class.curves
    vertex_degrees = [0] * isogeny_matrix.nrows()
    curve_map = [0] * isogeny_matrix.nrows()  # the mapping from curves to the numbering in the graph
    for ind, row in enumerate(isogeny_matrix):
        for n in row:
            if n.is_prime():
                 vertex_degrees[ind] += 1
    
    if len(isogeny_matrix[0]) == 6:
    # there are two possible graphs:
    # both have two vertices of order 3, but
    # one has 4 order 1 versices,
    # and the other has four order 2 vertices.
    # First we have to find which graph we have.
        degree_1_vertices = []
        degree_2_vertices = []
        degree_3_vertices = []
        for row in range(6):
            if vertex_degrees[row] == 3:
                degree_3_vertices.append(row)
            elif vertex_degrees[row] == 1:
                degree_1_vertices.append(row)
                the_graph_type = 'H'
            elif vertex_degrees[row] == 2:
                degree_2_vertices.append(row)
                the_graph_type = 'G'
        # we call vertices 1 and 2 the degree 3 vertices
        curve_map[0] = degree_3_vertices[0]
        curve_map[1] = degree_3_vertices[1]

        print "the_graph_type", the_graph_type

        if the_graph_type == 'G':
            print "the degree 3 vertices are",degree_3_vertices
            found_first_neighbor = False
            for ind, n in enumerate(isogeny_matrix[degree_3_vertices[0]]):
                print "xx", ind, n, degree_3_vertices
                if n.is_prime() and ind not in degree_3_vertices:
                    if not found_first_neighbor:
                        curve_map[2] = ind
                        degree_2_vertices.append(ind)
                        found_first_neighbor = True
                    else:
                        curve_map[4] = ind
                        degree_2_vertices.append(ind)

            for ind, n in enumerate(isogeny_matrix[degree_3_vertices[1]]):
                print "yy", ind, n
                if n.is_prime() and ind not in degree_3_vertices:
                    if isogeny_matrix[curve_map[2]][ind].is_prime():
                        print "                ind", ind, isogeny_matrix[curve_map[2]]
                        curve_map[3] = ind
                        degree_2_vertices.append(ind)
                    else:
                        curve_map[5] = ind
                        degree_2_vertices.append(ind)

        elif the_graph_type == 'H':
            print "the degree 3 vertices are",degree_3_vertices
            found_first_neighbor = False
            for ind, n in enumerate(isogeny_matrix[degree_3_vertices[0]]):
                print "xx", ind, n, degree_3_vertices
                if n.is_prime() and ind not in degree_3_vertices:
                    if not found_first_neighbor:
                        curve_map[2] = ind
                        found_first_neighbor = True
                    else:
                        curve_map[3] = ind
            found_first_neighbor = False
            for ind, n in enumerate(isogeny_matrix[degree_3_vertices[1]]):
                print "yy", ind, n
                if n.is_prime() and ind not in degree_3_vertices:
                    if not found_first_neighbor:
                        curve_map[4] = ind
                        found_first_neighbor = True
                    else:
                        curve_map[5] = ind

        else:
            for j in range(6):
                curve_map[j] = j

        this_graph = graph_type[the_graph_type]

        this_graph = this_graph.replace("_edgecolor_", "#333") # was #3d8
        this_graph = this_graph.replace("_degreecolor_", "#333") # was #d0d
        this_graph = this_graph.replace("_labelcolor_", "#1565C0") # was #3a3
        this_graph = this_graph.replace("_cardbordercolor_", "#333") # was #900

        for j in range(6):
            this_graph = this_graph.replace("_curve" + str(j) + "_", str(curve_map[j] + 1))
            this_graph = this_graph.replace("_curve" + str(j) + "degree" + "_", str(isogeny_class.curves[curve_map[j]]['degree']))
            this_graph = this_graph.replace("_curve" + str(j) + "torsion" + "_", str(isogeny_class.curves[curve_map[j]]['torsion_structure']))
            this_graph = this_graph.replace("_curve" + str(j) + "tamagawa" + "_", str(isogeny_class.curves[curve_map[j]]['tamagawa_product']))
            this_graph = this_graph.replace("_curve" + str(j) + "sha" + "_", str(isogeny_class.curves[curve_map[j]]['sha']))
            this_graph = this_graph.replace("_curve" + str(j) + "urlcremona" + "_", str(isogeny_class.curves[curve_map[j]]['curve_url_cremona']))
            this_graph = this_graph.replace("_curve" + str(j) + "label" + "_", str(isogeny_class.curves[curve_map[j]]['label']))
            if isogeny_class.curves[curve_map[j]]['optimal']:
                this_graph = this_graph.replace("_optimal" + str(j) + "" + "_", "optimal")
            else:
                this_graph = this_graph.replace("_optimal" + str(j) + "" + "_", "notoptimal")

            print "j is",j, isogeny_class.curves[curve_map[j]]['degree']

        return this_graph
    else:
        return graphG
