#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
#include <curl/curl.h>
size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

int main() {

    std::ifstream configFile("config.json");
    if (!configFile.is_open()) {
        std::cerr << "Failed to open config.json" << std::endl;
        return 1;
    }
    nlohmann::json config;
    configFile >> config;

    std::string url = config["url"];
    std::string readBuffer;

    CURL* curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
        CURLcode res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);


        std::ofstream outFile("output.html");
        outFile << readBuffer;
        outFile.close();
        
        std::cout << "Saved to output.html" << std::endl;
    } else {
        std::cerr << "Cannot initialize curl" << std::endl;
    }
    return 0;
}