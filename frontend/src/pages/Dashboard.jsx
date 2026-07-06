import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import GmailSelector from "../components/GmailSelector";
import RecipientSelector from "../components/RecipientSelector";
import InstructionBox from "../components/InstructionBox";
import DraftEditor from "../components/DraftEditor";

import {
  connectGoogleAccount,
  getConnectedAccounts,
} from "../services/googleAuth";

import {
  generateDraft,
  sendEmail,
} from "../services/langflow";

export default function Dashboard() {
  const [accounts, setAccounts] = useState([]);
  const [recipients, setRecipients] = useState([]);
  const [selectedAccount, setSelectedAccount] = useState("");

  const [instruction, setInstruction] = useState("");

  const [draft, setDraft] = useState({
    subject: "",
    body: "",
  });

  useEffect(() => {
    loadAccounts();
  }, []);

  async function loadAccounts() {
    try {
      const result = await getConnectedAccounts();

      setAccounts(result.accounts);

      if (result.accounts.length > 0) {
        setSelectedAccount(result.accounts[0]);
      }
    } catch (error) {
      console.error(error);
    }
  }

  async function connectAccount() {
    try {
      await connectGoogleAccount();
      await loadAccounts();
    } catch (error) {
      console.error(error);
    }
  }

  async function handleGenerateDraft() {
    console.log("Generate button clicked");

    if (!instruction.trim()) {
      console.log("Instruction is empty");
      return;
    }

    console.log("Instruction:", instruction);

    try {
      console.log("Calling Langflow...");

      const generatedDraft = await generateDraft(instruction);
      
      console.log(generatedDraft);

      setRecipients(generatedDraft.recipients);

      setDraft({
        subject: generatedDraft.subject,
        body: generatedDraft.body,
      });      

      console.log("Draft updated.");
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function handleSendEmail() {
    if (!selectedAccount) {
      alert("Please select a Gmail account.");
      return;
    }

    if (recipients.length === 0) {
      alert("No recipients found.");
      return;
    }

    if (!draft.subject.trim() || !draft.body.trim()) {
      alert("Draft is empty.");
      return;
    }

    try {
      const result = await sendEmail({
        sender: selectedAccount,
        recipients,
        subject: draft.subject,
        body: draft.body,
      });

      console.log("Send Flow Result:");
      console.log(result);

      alert("Email request completed.");
    } catch (error) {
      console.error(error);
      alert("Failed to send email.");
    }
  }

  return (
    <div className="min-h-screen bg-slate-100">

      <Navbar />

      <div className="max-w-5xl mx-auto p-8">

        <GmailSelector
          accounts={accounts}
          selectedAccount={selectedAccount}
          onSelect={setSelectedAccount}
          onConnect={connectAccount}
        />

        <RecipientSelector />

        <InstructionBox
          instruction={instruction}
          setInstruction={setInstruction}
          onGenerate={handleGenerateDraft}
        />

        <DraftEditor
          draft={draft}
          setDraft={setDraft}
          onSend={handleSendEmail}
        />

      </div>

    </div>
  );
}