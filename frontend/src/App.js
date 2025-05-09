import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || "");
  const [pouzivatel, setPouzivatel] = useState(localStorage.getItem("meno") || "");
  const [meno, setMeno] = useState("");
  const [heslo, setHeslo] = useState("");
  const [jeRegistracia, setJeRegistracia] = useState(false);

  const [ulohy, setUlohy] = useState([]);
  const [nazov, setNazov] = useState("");
  const [popis, setPopis] = useState("");

  useEffect(() => {
    if (token) {
      nacitajUlohy();
    }
  }, [token]);

  const nacitajUlohy = async () => {
    try {
      const odpoved = await fetch("http://127.0.0.1:5000/tasks", {
        headers: { Authorization: `Bearer ${token}` }
      });
      const data = await odpoved.json();
      setUlohy(data);
    } catch (err) {
      console.error("Chyba pri načítaní úloh:", err);
    }
  };

  const pridajUlohu = async () => {
    if (!nazov || !popis) return alert("Zadaj názov aj popis.");
    try {
      await fetch("http://127.0.0.1:5000/tasks", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({ nazov, popis })
      });
      setNazov("");
      setPopis("");
      nacitajUlohy();
    } catch (err) {
      console.error("Chyba pri pridávaní úlohy:", err);
    }
  };

  const zmenStav = async (id, novyStav) => {
    try {
      await fetch(`http://127.0.0.1:5000/tasks/${id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({ stav: novyStav })
      });
      nacitajUlohy();
    } catch (err) {
      console.error("Chyba pri zmene stavu:", err);
    }
  };

  const odstranUlohu = async (id) => {
    if (!window.confirm("Naozaj chceš úlohu vymazať?")) return;
    try {
      await fetch(`http://127.0.0.1:5000/tasks/${id}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` }
      });
      nacitajUlohy();
    } catch (err) {
      console.error("Chyba pri odstraňovaní úlohy:", err);
    }
  };

  const prihlasPouzivatela = async () => {
    if (!meno || !heslo) return alert("Zadaj meno aj heslo.");
    try {
      const odpoved = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ meno, heslo })
      });
      const data = await odpoved.json();
      if (data.token) {
        localStorage.setItem("token", data.token);
        localStorage.setItem("meno", meno);
        setToken(data.token);
        setPouzivatel(meno);
      } else {
        alert("Prihlásenie zlyhalo.");
      }
    } catch (err) {
      console.error("Chyba pri prihlasovaní:", err);
    }
  };

  const registrujPouzivatela = async () => {
    if (!meno || !heslo) return alert("Zadaj meno aj heslo.");
    try {
      const odpoved = await fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ meno, heslo })
      });
      const data = await odpoved.json();
      if (odpoved.status === 201) {
        alert("Registrácia úspešná, môžeš sa prihlásiť.");
        setJeRegistracia(false);
      } else {
        alert(data.error || "Chyba pri registrácii.");
      }
    } catch (err) {
      console.error("Chyba pri registrácii:", err);
    }
  };

  const odhlas = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("meno");
    setToken("");
    setPouzivatel("");
    setMeno("");
    setHeslo("");
    setUlohy([]);
  };

  const renderUlohy = (stav) => (
    ulohy.filter(u => u.stav === stav).map(u => (
      <li key={u.id}>
        <strong>{u.nazov}</strong>: {u.popis} | Stav: {u.stav}
        {stav === "Nezahájená" && (
          <>
            <button onClick={() => zmenStav(u.id, "Prebieha")}>Prebieha</button>
            <button onClick={() => odstranUlohu(u.id)}>Odstrániť</button>
          </>
        )}
        {stav === "Prebieha" && (
          <>
            <button onClick={() => zmenStav(u.id, "Hotová")}>Hotová</button>
            <button onClick={() => odstranUlohu(u.id)}>Odstrániť</button>
          </>
        )}
        {stav === "Hotová" && (
          <button onClick={() => odstranUlohu(u.id)}>Odstrániť</button>
        )}
      </li>
    ))
  );

  if (!token) {
    return (
      <div style={{ padding: "20px" }}>
        <h2>{jeRegistracia ? "Registrácia" : "Prihlásenie"}</h2>
        <input
          type="text"
          placeholder="Zadaj meno"
          value={meno}
          onChange={(e) => setMeno(e.target.value)}
        />
        <input
          type="password"
          placeholder="Zadaj heslo"
          value={heslo}
          onChange={(e) => setHeslo(e.target.value)}
        />
        {jeRegistracia ? (
          <>
            <button onClick={registrujPouzivatela}>Registrovať</button>
            <p>
              Už máš účet?{" "}
              <button onClick={() => setJeRegistracia(false)}>Prihlásiť sa</button>
            </p>
          </>
        ) : (
          <>
            <button onClick={prihlasPouzivatela}>Prihlásiť</button>
            <p>
              Nemáš účet?{" "}
              <button onClick={() => setJeRegistracia(true)}>Registrovať sa</button>
            </p>
          </>
        )}
      </div>
    );
  }

  return (
    <div style={{ padding: "20px" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h1>Task Manager 2.0 – React Frontend</h1>
        <div>
          <span style={{ marginRight: "10px" }}>👤 {pouzivatel}</span>
          <button onClick={odhlas}>Odhlásiť</button>
        </div>
      </div>

      <input
        type="text"
        placeholder="Zadaj názov"
        value={nazov}
        onChange={(e) => setNazov(e.target.value)}
      />
      <input
        type="text"
        placeholder="Zadaj popis"
        value={popis}
        onChange={(e) => setPopis(e.target.value)}
      />
      <button onClick={pridajUlohu}>Pridať</button>

      <h2>🕒 Nezahájené úlohy</h2>
      <ul>{renderUlohy("Nezahájená")}</ul>

      <h2>🌺 Prebiehajúce úlohy</h2>
      <ul>{renderUlohy("Prebieha")}</ul>

      <h2>✅ Hotová úlohy</h2>
      <ul>{renderUlohy("Hotová")}</ul>
    </div>
  );
}

export default App;
