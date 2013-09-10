/* In this example we want to test the type of data that can be serialized to be
 * used as vertex/edge of the GraphLab's graph data structure. For the edges we
 * will use the empty data type and for the vertices a particle type for the
 * particle filter in the CGR algorithm. */

#include <graphlab.hpp>

template <class num>
class vector2d{
public:
  num x,y;

  vector2d()
    {}
  vector2d(num nx,num ny)
    {x=nx; y=ny;}

  /// set the components of the vector
  void set(num nx,num ny)
    {x=nx; y=ny;}
  /// set the components of the vector to the same value
  void setAll(num nx)
    {x=y=nx;}
  /// set the components of the vector
  template <class vec> void set(vec p)
    {x=p.x; y=p.y;}
  /// zero all components of the vector void zero()
  void zero()
    {x=y=0;}

  /// copy constructor
  vector2d<num> &operator=(vector2d<num> p)
    {set(p); return(*this);}

  /// copy constructor from compatible classes
  template <class vec> vector2d<num> &operator=(vec p)
    {set(p.x,p.y); return(*this);}
    
  /// element accessor
  num &operator[](int idx)
    {return(((num*)this)[idx]);}
  const num &operator[](int idx) const
    {return(((num*)this)[idx]);}
};

typedef vector2d<float> vector2f;

class Particle2D {
  public:
    vector2f loc, lastLoc;
    float angle;
    float weight;

  public:
    Particle2D() {weight = angle = 0.0; loc.zero();}

    Particle2D(float _x, float _y, float _theta, float _w) { loc.set(_x,_y); lastLoc.set(-DBL_MAX,-DBL_MAX); angle = _theta; weight = _w;}

    Particle2D(vector2f _loc, float _theta, float _w) { loc = _loc; angle = _theta; weight = _w;}

    bool operator<(const Particle2D &other) {return weight<other.weight;}

    bool operator>(const Particle2D &other) {return weight>other.weight;}

    Particle2D &operator=(const Particle2D &other) {
      angle = other.angle;
      weight = other.weight;
      loc.x = other.loc.x;
      loc.y = other.loc.y;
      lastLoc.x = other.lastLoc.x;
      lastLoc.y = other.lastLoc.y;
      return *this;
    }

    void save(graphlab::oarchive& oarc) const {
      oarc << angle << weight << loc.x << loc.y << lastLoc.x << lastLoc.y;
    }

    void load(graphlab::iarchive& iarc) {
      iarc >> angle >> weight >> loc.x >> loc.y >> lastLoc.y >> lastLoc.y;
    }
};

typedef graphlab::distributed_graph<Particle2D, graphlab::empty> graph_type;

int main(int argc, char** argv) {
  graphlab::mpi_tools::init(argc, argv);
  graphlab::distributed_control dc;

  graph_type graph(dc);

  graphlab::mpi_tools::finalize();

  return 0;
}
