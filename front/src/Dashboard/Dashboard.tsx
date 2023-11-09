import React, { useState, useEffect } from "react";
import { Button, TextInput, AreaChart } from "@tremor/react";
import { MagnifyingGlassIcon } from "@heroicons/react/24/outline";
import { get_str } from "../functions/utils";

const REACT_APP_SCRAPESTORM_API_KEY = process.env.REACT_APP_SCRAPESTORM_API_KEY;
const REACT_APP_SCRAPESTORM_API_USER =
  process.env.REACT_APP_SCRAPESTORM_API_USER;
const REACT_APP_SCRAPESTORM_API_MEDIA =
  process.env.REACT_APP_SCRAPESTORM_API_MEDIA;
const REACT_APP_SCRAPESTORM_API_TIMEOUT =
  process.env.REACT_APP_SCRAPESTORM_API_TIMEOUT;

const SESSION_STORAGE_USER_PREFIX = "insta_user_";

const Dashboard = () => {
  const [searchText, setSearchText] = useState<string>("");
  const [instaName, setInstaName] = useState<string>("");

  const api_get = (): object => {
    let result: object = {};
    let apiKey: string = REACT_APP_SCRAPESTORM_API_KEY
      ? REACT_APP_SCRAPESTORM_API_KEY
      : "";
    console.log(apiKey);
    let timeout: number = REACT_APP_SCRAPESTORM_API_TIMEOUT
      ? parseInt(REACT_APP_SCRAPESTORM_API_TIMEOUT) * 1000
      : 60000;
    console.log(timeout);
    const params: Record<string, string> = {
      token: apiKey,
      username: instaName,
    };
    const headers = {
      "Content-Type": "application/json",
    };

    const queryString = new URLSearchParams(params).toString();
    const fullUrl = `${REACT_APP_SCRAPESTORM_API_USER}?${queryString}`;

    const fetchOptions = {
      method: "GET",
      headers: headers,
    };

    const controller = new AbortController();
    const signal = controller.signal;

    const timeoutId = setTimeout(() => {
      controller.abort();
    }, timeout);

    fetch(fullUrl, { ...fetchOptions, signal })
      .then((response) => {
        clearTimeout(timeoutId);
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        return result;
      })
      .catch((error) => {
        if (error.name === "AbortError") {
          console.error("Request timed out");
        } else {
          console.error("Error:", error);
        }
      });
    return {};
  };

  useEffect(() => {
    if (instaName !== "") {
      console.log("api:" + REACT_APP_SCRAPESTORM_API_USER);

      let result: object;

      const storageLabel = SESSION_STORAGE_USER_PREFIX + instaName;
      let data: string = get_str(sessionStorage.getItem(storageLabel));

      if (data === "") {
        result = api_get();
        sessionStorage.setItem(storageLabel, JSON.stringify(result));
        console.log("saved");
      } else {
        result = JSON.parse(data);
        console.log("loaded");
      }
      console.log(result);
    }
    return () => {
      // Perform any clean-up or unsubscribe actions here
    };
  }, [instaName]);

  const handleSearch = () => {
    // console.log("search: " + searchText);
    setInstaName(searchText);
  };

  const handleSearchTextChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    // console.log(e.target.value);
    setSearchText(e.target.value);
  };

  const handleOnKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      handleSearch();
    }
  };

  return (
    <div className="flex flex-col justify-center items-center w-full">
      <div className="flex flex-row mx-4 w-full ">
        <TextInput
          className="m-2"
          type="text"
          placeholder="Search..."
          value={searchText}
          onChange={handleSearchTextChange}
          onKeyPress={handleOnKeyPress}
        />
        <Button
          className="m-2"
          size="sm"
          onClick={handleSearch}
          variant="primary"
          icon={MagnifyingGlassIcon}
        >
          Search
        </Button>
      </div>
      <div className="border-b-2 border-red-100 pb-2">
        <h1>222</h1>
      </div>
    </div>
  );
};

export default Dashboard;
