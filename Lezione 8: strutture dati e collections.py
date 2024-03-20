'''
DICTIONARIES:

mappano una chiave a un valore, la chiave deve essere hashable, cioè una funzione __hash__
(va definita nel momento in cui tu crei un oggetto che userai come chiave) trasforma la chiave in un
numero (che può essere comparato), una buona funzione di hash evita collisioni (due hash uguali che si riferiscono a
oggetti diversi)

DEFAULTDICT (collections.defaultdict)
contiene un valore di default che viene restituito ogni volta che si cerca di accedere a una chiave
che nel dizionario non esiste, quindi non ottieni mai l'eccezione keyError ma un valore di default che scegli

MAPPING PROXY TYPE (types.MappingProxyType)
Crea un dizionario read-only, modificandone uno esistente, cancella i metodi che modificano il dizionario
dizionario_read_only = types.MappingProxyType(dizionario_normale)

ARRAY TYPES (sequenze):
list, str, tuple

array.array ti obbliga a dichiarare qual'è il tipo: arr = array.array("f", (1.0...))

RECORDS:
contenitore di dati a loro volta articolati su più campi, oggetti e classi ad esempio

collections.nametuple è una tupla che ha come indici non numerici ma attributi
Car = collections.nametuple("Car", ("name", "year")) ti permette di creare una tupla così:
c1 = Car("Panda", 2019) e poi anche di chiamare gli attributi con il punto
(simile a dataclass)

SETS (INSIEMI)
Contenitore mutabile di oggetti hashable, un in set non puo essere usato in un altro set, la sintassi è {1,2,3}
non sono permessi duplicati
Frozenset: immutabile, può essere usato come chiave di un dizionario o elemento di un set (è hashable)
conviene costruirlo a partire da un set già definito

"Multiset"
collections.Counter() un counter è un oggetto che conta le ricorrenze degli oggetti nella struttura dati
che gli viene fornita, gli elementi di un counter devono essere immutabili (devono essere confrontabili)
la classe counter si può inizializzare con oggetti Iterables
L'oggetto counter ha dei metodi utili tipo .most_common() che ritorna l'oggetto che compare di più

QUEUES AND STACKS
FIFO -> Queue (coda), gli elementi vengono estratti nell'ordine in cui sono arrivati, aggiungo un elemento sempre
dallo stesso lato ed estraggo sempre dal lato opposto
LIFO -> Stack (pila di oggetti), gli elementi estratti sono gli ultimi a essere stati aggiunti, il lato da cui
si aggiunge è sempre lo stesso ed è uguale a quello da cui estraggo (add -> "push", extract -> "pop")

Una lista che utilizza append() per aggiungere e pop(index) per estrarre si comporta come una coda fifo
Una lista che utilizza append() e pop() è uno stack con funzionamento lifo, senza problemi

Deque (double ended queue) -> collections.deque(), ha in più i metodi appendleft() e popleft() che implementano i due
metodi anche per l'altro lato della lista senza tempi più lunghi come sarebbe fare un pop(0) (stessa efficienza)
il deque è top per fare una queue fifo usando due metodi opposti. Deque ha anche metodi utili

PRIORITY QUEUES
Gli elementi vengono aggiunti man mano che arrivano ma verranno estratti sulla base di una priorità,
sono quindi confrontabili e deve essere definito il metodo < (__lt__), l'idea è trovare l'elemento
minimo ed estrarlo, dove il minimo corrisponde a un attributo di priorità

queue.PriorityQueue, puoi usare put() che inserisce gli elementi e get_nowait() che restituisce il minimo (efficiente)

heapq che si crea facendo h = heapify(iterable) che ti implementa delle funzioni e non degli oggetti come prima,
viene implementato heapq.heappush(h, x) dove h è la lista e x l'oggetto da immettere e heapq.heappop(h)
dove h è la lista. Heap è basata su una struttura gerarchica ad albero (treemap) in cui il primo elemento è sempre
il minimo e gli altri seguono regole più strane



'''
