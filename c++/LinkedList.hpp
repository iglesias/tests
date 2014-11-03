#include <cstddef>

template<class T>
class LinkedList
{
	public:
		LinkedList() : _node(nullptr) { };

		void push_back(const T& d)
		{
			if (_node==nullptr)
			{
				_node = new Node(d, nullptr);
			}
			else
			{
				Node* prev = _node;
				Node* cur = prev->next();
				while (cur!=nullptr)
				{
					prev = cur;
					cur = cur->next();
				}

				cur = new Node(d, nullptr);
				prev->next() = cur;
			}
		}

		virtual ~LinkedList()
		{
			while (_node!=nullptr)
			{
				Node* aux = _node->next();
				delete _node;
				_node = aux;
			}
		}

	private:
		struct Node
		{
			public:
				Node(T data, Node* next) : _data(data), _next(next) { }
				Node*& next() { return _next; }

			private:
				T _data;
				Node* _next;
		};

	private:
		Node* _node;
};
