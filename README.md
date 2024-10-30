# AmygdalaGPT

AmygdalaGPT is a memory-augmented LLM system that provides persistent memory capabilities to large language models through a dedicated memory management agent and SQL database integration.

## 🧠 Concept

AmygdalaGPT enhances traditional LLMs by implementing a biological memory-inspired architecture:

### Memory Agent
The core of the system is an intelligent agent that manages both long-term and short-term memory, similar to human memory processes:

- **Memory Analysis**: For each incoming request, the agent:
  1. Evaluates potential new information to learn
  2. Determines relevant memory segments to access
  3. Updates short-term memory based on conversation context

- **Memory Types**:
  - **Long-term Memory**: Persistent SQL database storing structured information about:
    - Persons
    - Places
    - Jobs
    - Mathematical concepts
    - Historical interactions
    - Domain-specific knowledge
  
  - **Short-term Memory**: Dynamic context window containing:
    - Most relevant information to current conversation
    - Abstracted knowledge representations
    - Limited to user-specified token count
    - Continuously updated based on conversation flow

## 🚀 Getting Started

### Prerequisites
- Docker ... thats it 🤩🤩

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/AmygdalaGPT.git
cd AmygdalaGPT

# Configure environment
cp .env.example .env
# Edit .env with your API keys and configuration
```

### Configuration
##### 1) Define the required environment variables in `.env` like MISTRAL_API_KEY

##### 2) Make bin scripts executables:
```
chmod +x bin/build
chmod +x bin/run
chmod +x bin/stop
chmod +x bin/shell
```

### Run
##### 1) Open terminal in the container:
```
bin/shell
```
##### 2) Run main.py in the terminal:
```
python main.py
```

## 📚 Features

### Memory Management
- **Intelligent Information Extraction**: Automatically identifies and stores relevant information from conversations
- **Context-Aware Retrieval**: Efficiently searches and retrieves relevant information based on current conversation
- **Dynamic Memory Optimization**: Maintains optimal short-term memory by removing irrelevant information

### Database Integration
- **Structured Data Storage**: Organized storage of different types of information
- **Efficient Querying**: Optimized database queries for quick information retrieval
- **Automatic Schema Evolution**: Adapts database structure based on new types of information

### Response Generation
- **Context-Aware Responses**: Generates responses based on both current input and historical knowledge
- **Memory-Augmented Output**: Enriches responses with relevant historical context
- **Consistency Maintenance**: Ensures responses align with previously stored information

## 🤝 Contributing

Contributions are welcome!

## 📝 License

This project is licensed under the MIT License.

## 📞 Contact

- Project Maintainer - [Ashraf Beshtawi](mailto:beshtawi.ashraf@gmail.com)
- Project Homepage - [GitHub Repository](https://github.com/ashrafbeshtawi/AmygdalaGPT)

## 🙏 Acknowledgments

- Inspired by human memory processes and cognitive architecture
- Built with [Mistral AI](https://mistral.ai/) technology
- Special thanks to the open-source community